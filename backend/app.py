from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.api import api_blueprint

app = Flask(__name__)
CORS(app)

# Registrar las rutas de la API
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
