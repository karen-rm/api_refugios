from flask import jsonify
from werkzeug.exceptions import HTTPException
import traceback

def register_error_handlers(app):

    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        return jsonify({
            "error": error.name,
            "mensaje": error.description,
            "status": error.code
        }), error.code

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        print("ERROR INTERNO:") 
        print(error) 
        traceback.print_exc()

        return jsonify({
            "error": "Internal Server Error",
            "mensaje": "Ocurrió un error interno en el servidor",
            "status": 500
        }), 500