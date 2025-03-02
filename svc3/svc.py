from flask import Flask, jsonify
import requests
import logging
import time

logging.basicConfig(filename='svc.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

healthy = True

@app.route('/start')
def start():
    global healthy
    url = 'http://svc2:5002/data' # svc2 URL
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            number = int(data['number'])
            logging.info(f"Received number: {number}.")
            print(f"Received number: {number}.")
        else:
            healthy = False
            logging.error(f"Error: {response.status_code}")
            print(f"Error: {response.status_code}")
        time.sleep(1)

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
    
@app.route('/viewlogs3')
def viewlogs3():
    with open('svc.log', 'r') as f:
        lines = f.readlines()
        last_15_lines = lines[-15:]
        return ''.join(last_15_lines)
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5003)
    logging.info(f"Server listening on localhost:5003")