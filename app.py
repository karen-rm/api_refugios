from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request


from app.models.models import db 


load_dotenv()

app = Flask(__name__)
CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Conexión db
db.init_app(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok", 
        "mensaje": "API de Refugios funcionando"
    }), 200


if __name__ == '__main__':
    app.run(debug=True)