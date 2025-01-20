from flask import Flask
from flask_cors import CORS
from app.routes import items_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(items_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)