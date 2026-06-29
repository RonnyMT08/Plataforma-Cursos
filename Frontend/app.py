from flask import Flask
from routes.public import register as register_public

app = Flask(__name__)

register_public(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)