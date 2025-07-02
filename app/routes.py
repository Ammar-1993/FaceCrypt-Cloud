from flask import Blueprint, render_template, request, redirect, url_for
from app.config import db, bucket

bp = Blueprint('routes', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "❌ No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "❌ No selected file", 400

    # رفع إلى Firebase Storage
    blob = bucket.blob(file.filename)
    blob.upload_from_file(file)

    # حفظ رابط في Firestore
    doc_ref = db.collection('uploads').document()
    doc_ref.set({
        'filename': file.filename,
        'url': blob.public_url
    })

    return f"✅ Uploaded {file.filename} successfully!"
