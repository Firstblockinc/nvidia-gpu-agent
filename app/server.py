import logging
from flask import Flask, jsonify
from .gpu_manager import get_gpu_info

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    logging.info("Received request for GPU data.")
    try:
        data = get_gpu_info()
        logging.info("Successfully retrieved GPU data.")
        return jsonify(data)
    except Exception as e:
        logging.error(f"Error retrieving GPU data: {e}")
        return jsonify({"error": "Failed to retrieve GPU data"}), 500

def run_server():
    logging.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
