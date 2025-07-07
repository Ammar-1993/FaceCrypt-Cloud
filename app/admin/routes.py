from flask import Blueprint, request, jsonify, render_template
from app.config import ADMIN_PASSWORD, db
from utils import face_utils, firebase_utils

# ✅ إنشاء الـ Blueprint
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# ✅ صفحة Admin Portal
@admin_bp.route('/', methods=['GET'])
def admin_portal():
    return render_template('index_admin.html')

# ✅ /admin/login
@admin_bp.route('/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    if not data or 'password' not in data:
        firebase_utils.log_audit_event('admin', 'ADMIN_LOGIN', status='failure', ip_address=request.remote_addr)
        return jsonify({"error": "❌ Password required"}), 400

    password = data['password']
    if password == ADMIN_PASSWORD:
        firebase_utils.log_audit_event('admin', 'ADMIN_LOGIN', status='success', ip_address=request.remote_addr)
        return jsonify({"message": "✅ Welcome, Admin"}), 200
    else:
        firebase_utils.log_audit_event('admin', 'ADMIN_LOGIN', status='failure', ip_address=request.remote_addr)
        return jsonify({"error": "Invalid Password"}), 403

# ✅ /admin/add_user
@admin_bp.route('/add_user', methods=['POST'])
def admin_add_user():
    user_id = request.form.get('user_id')
    name = request.form.get('name')
    email = request.form.get('email')
    image_file = request.files.get('image')

    if not user_id or not name or not email or not image_file:
        return jsonify({"error": "❌ Missing required fields"}), 400

    try:
        image_array = face_utils.load_image_from_request(image_file)
        encoding = face_utils.extract_face_encoding(image_array)

        user_data = {
            "name": name,
            "email": email,
            "face_encoding": encoding.tolist(),
            "failed_attempts": 0,
            "soft_block": False,
            "blocked": False
        }

        firebase_utils.add_user_to_firestore(user_id, user_data)
        return jsonify({"message": "✅ User was added successfully"}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"❌ Internal server error: {str(e)}"}), 500

# ✅ /admin/delete_user
@admin_bp.route('/delete_user', methods=['POST'])
def admin_delete_user():
    data = request.get_json()
    if not data or 'user_id' not in data:
        return jsonify({"error": "❌ user_id is required"}), 400

    user_id = data['user_id']

    try:
        firebase_utils.delete_user_from_firestore(user_id)
        return jsonify({"message": "✅ User was deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"❌ Internal server error: {str(e)}"}), 500

# ✅ /admin/list_users
@admin_bp.route('/list_users', methods=['GET'])
def admin_list_users():
    try:
        users = firebase_utils.get_all_users()
        response = [{
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "blocked": user.get("blocked", False),
            "soft_block": user.get("soft_block", False),
            "failed_attempts": user.get("failed_attempts", 0)
        } for user in users]

        return jsonify({"users": response}), 200

    except Exception as e:
        return jsonify({"error": f"❌ Internal server error: {str(e)}"}), 500

# ✅ /admin/audit_logs
@admin_bp.route('/audit_logs', methods=['GET'])
def admin_audit_logs():
    try:
        logs_ref = db.collection('audit_logs')
        docs = logs_ref.stream()

        logs = []
        for doc in docs:
            log = doc.to_dict()
            log['id'] = doc.id
            logs.append(log)

        return jsonify({"logs": logs}), 200

    except Exception as e:
        return jsonify({"error": f"❌ Internal server error: {str(e)}"}), 500
