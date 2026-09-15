from flask import jsonify


def health_check():
    return jsonify({
        "status": "ok",
        "mensaje": "API de Refugios funcionando"
    }), 200