# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify
from controller import main
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        # El cliente debe enviar un JSON con la clave "file" que contenga el base64
        data = request.get_json()
        if not data or "file" not in data:
            return jsonify({"error": "No se recibió archivo en base64"}), 400

        print(data)
        
        result = main(data["file"])
        
        return jsonify({
            "message": "Imagen procesada correctamente",
            "data": int(result)
        }), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route("/hello", methods=["GET"])
def hello_world():
    try:
        return jsonify({"message": "Hello world!"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000)
