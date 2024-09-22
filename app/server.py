from flask import Flask, jsonify
from .gpu_manager import get_gpu_info

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    data = get_gpu_info()
    return jsonify(data)

def run_server():
    app.run(host='0.0.0.0', port=5000)  
