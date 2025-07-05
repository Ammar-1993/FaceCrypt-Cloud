from flask import Blueprint, request, jsonify
from utils import face_utils, firebase_utils

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/add', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'user_id' not in data or 'user_data' not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_id = data['user_id']
    user_data = data['user_data']

    firebase_utils.add_user_to_firestore(user_id, user_data)
    return jsonify({"message": f"✅ User {user_id} added successfully."})

@users_bp.route('/delete', methods=['POST'])
def delete_user():
    data = request.json
    if not data or 'user_id' not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_id = data['user_id']
    firebase_utils.delete_user_from_firestore(user_id)
    return jsonify({"message": f"✅ User {user_id} deleted successfully."})

@users_bp.route('/list', methods=['GET'])
def list_users():
    users = firebase_utils.get_all_users()
    return jsonify({"users": users})

@users_bp.route('/verify_login', methods=['POST'])
def verify_login():
    if 'image' not in request.files:
        return jsonify({"error": "❌ No image provided"}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({"error": "❌ Empty file name"}), 400

    try:
        # ✅ Load image from request
        image_array = face_utils.load_image_from_request(image_file)
        
        # ✅ Extract face encoding
        new_encoding = face_utils.extract_face_encoding(image_array)
        
        # ✅ جلب جميع المستخدمين
        users = firebase_utils.get_all_users()

        print(f"✅ Retrieved {len(users)} users from Firestore")

        # ✅ مقارنة الوجه الجديد مع جميع المستخدمين
        matched_user = None
        for user in users:
            # ✅ تحقق من حالة الحظر الدائم
            if user.get('blocked', False):
                continue  # حساب مغلق دائمًا

            stored_encoding = user.get('face_encoding')
            if stored_encoding is None:
                continue

            result = face_utils.compare_encodings(stored_encoding, new_encoding)
            if result:
                matched_user = user
                break

        # ✅ إذا وجدنا تطابق
        if matched_user:
            # ✅ إزالة عدد المحاولات
            user_id = matched_user['id']
            updated_data = {
                "failed_attempts": 0,
                "soft_block": False
            }
            firebase_utils.update_user_fields(user_id, updated_data)

            # ✅ تسجيل Audit Log
            firebase_utils.log_audit_event({
                "user_id": user_id,
                "status": "success",
                "event": "login",
            })

            return jsonify({
                "message": "✅ Access Granted",
                "user": {
                    "id": matched_user['id'],
                    "name": matched_user.get('name'),
                    "email": matched_user.get('email')
                }
            }), 200

        # ✅ إذا لم نجد تطابق – عالج سياسات الحظر
        # جرب كل المستخدمين غير المحظورين
        for user in users:
            user_id = user['id']
            if user.get('blocked', False):
                continue

            # زيادة عدد المحاولات
            failed_attempts = user.get('failed_attempts', 0) + 1
            update_data = {
                "failed_attempts": failed_attempts
            }

            # soft_block
            if failed_attempts == 3:
                update_data["soft_block"] = True

            # blocked
            if failed_attempts >= 5:
                update_data["blocked"] = True

            firebase_utils.update_user_fields(user_id, update_data)

        return jsonify({
            "message": "❌ Access Denied – No matching user found. Policy updated."
        }), 403

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"❌ Internal Error: {str(e)}"}), 500




