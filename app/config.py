import firebase_admin
from firebase_admin import credentials, firestore, storage

# مسار مفتاح الخدمة
SERVICE_ACCOUNT_PATH = 'firebase/serviceAccountKey.json'

# تهيئة Firebase Admin (مرة واحدة فقط)
firebase_app = None
db = None
bucket = None

def initialize_firebase():
    global firebase_app, db, bucket

    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
        firebase_app = firebase_admin.initialize_app(cred, {
            'storageBucket': 'facecryptcloud.appspot.com'
        })

    db = firestore.client()
    bucket = storage.bucket()

    print("✅ Firebase Admin SDK initialized in config.py")
