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
        
        
        # ✅ جلب كل المستخدمين المسجلين من Firestore
        users = firebase_utils.get_all_users()
         
        # ✅ طباعة اختبارية في اللوج
        print(f"✅ Retrieved {len(users)} users from Firestore")

        # ✅ ردهم مؤقتًا في الاستجابة
        return jsonify({
            "message": "✅ Image processed and users retrieved.",
            "num_users": len(users),
            "users": users
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"❌ Internal Error: {str(e)}"}), 500


