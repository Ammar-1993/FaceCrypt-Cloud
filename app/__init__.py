from flask import Flask
from app import config
from app.routes import bp as routes_bp

def create_app():
    app = Flask(__name__)

    # تهيئة Firebase
    config.initialize_firebase()

    # تسجيل المسارات
    app.register_blueprint(routes_bp)

    print("✅ Flask App created and routes registered.")
    return app
