import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    parametro = request.args.get('parametro', None)
    dato = os.getenv("DATO", "NULO")
    if not parametro:
        return jsonify({"error": "Parametro no proporcionado"}), 400
    return jsonify({"parametro": parametro, "dato": dato})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)