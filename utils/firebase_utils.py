from firebase_admin import firestore
from app.config import db

def add_user_to_firestore(user_id, user_data):
    """
    يضيف مستخدمًا جديدًا إلى Firestore
    """
    doc_ref = db.collection('users').document(user_id)
    doc_ref.set(user_data)
    print(f"✅ User {user_id} added to Firestore.")

def delete_user_from_firestore(user_id):
    """
    يحذف مستخدمًا من Firestore
    """
    doc_ref = db.collection('users').document(user_id)
    doc_ref.delete()
    print(f"✅ User {user_id} deleted from Firestore.")

def get_all_users():
    """
    يجلب جميع المستخدمين من Firestore
    """
    users = []
    docs = db.collection('users').stream()
    for doc in docs:
        user = doc.to_dict()
        user['id'] = doc.id
        users.append(user)
    print(f"✅ Retrieved {len(users)} users.")
    return users

def log_audit_event(event_data):
    """
    يسجل حدث تدقيق (Audit Event) في Firestore
    """
    doc_ref = db.collection('audit_logs').document()
    doc_ref.set(event_data)
    print("✅ Audit event logged.")

def update_user_fields(user_id, data):
    doc_ref = db.collection('users').document(user_id)
    doc_ref.update(data)
    print(f"✅ Updated user {user_id} with: {data}")

