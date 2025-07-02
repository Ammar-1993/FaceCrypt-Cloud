from flask import Flask
from app.routes import bp

import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'templates')
)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
