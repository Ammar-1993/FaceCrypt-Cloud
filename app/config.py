import firebase_admin
from firebase_admin import credentials, firestore, storage

SERVICE_ACCOUNT_PATH = 'firebase/serviceAccountKey.json'

firebase_app = None
db = None
bucket = None

def initialize_firebase():
    global firebase_app, db, bucket

    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_app = firebase_admin.initialize_app(cred, {
            'storageBucket': 'facecryptcloud.firebasestorage.app'
        })
        print("✅ Firebase Admin SDK initialized in config.py")

    db = firestore.client()
    bucket = storage.bucket()

# ⚡ التهيئة التلقائية وقت الاستيراد!
initialize_firebase()
