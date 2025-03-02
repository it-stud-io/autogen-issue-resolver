from flask import Flask, jsonify
import logging
import random

logging.basicConfig(filename='svc.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

healthy = True

@app.route('/data')
def data():
    global healthy
    number = random.randint(1, 500)
    logging.info(f"Generated random number: {number}.")
    if number != 250:
        data = {
            "number": number
        }
        logging.info(f"Returning number: {number}.")
        return jsonify(data)
    else:
        healthy = False
        logging.error(f"Number is 250, raising exception.")
        raise Exception("Number is 250, shutting down server.")
    
@app.route('/health')
def health():
    global healthy
    if healthy:
        logging.info("Health check passed.")
        return jsonify({"status": "ok"})
    else:
        logging.error("Health check failed.")
        return jsonify({"status": "error"})

@app.route('/logs')
def logs():
    with open('svc.log', 'r') as f:
        return f.read()
    
@app.route('/viewlogs1')
def viewlogs1():
    with open('svc.log', 'r') as f:
        lines = f.readlines()
        last_15_lines = lines[-15:]
        return ''.join(last_15_lines)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
    logging.info(f"Server listening on localhost:5001")