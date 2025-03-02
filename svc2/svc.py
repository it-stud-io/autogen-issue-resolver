from flask import Flask, jsonify
import requests
import logging

logging.basicConfig(filename='svc.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

healthy = True

@app.route('/data')
def data():
    global healthy
    url = 'http://svc1:5001/data' # svc1 URL
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        number = int(data['number'])
        logging.info(f"Received number: {number}.")
        number += 50
        logging.info(f"Calculated number: {number}.")
        if number != 350:
            data = {
                "number": number
            }
            logging.info(f"Returning number: {number}.")
            return jsonify(data)
        else:
            healthy = False
            logging.error(f"Number is 350, raising exception.")
            raise Exception("Number is 350, shutting down server.")
    else:
        logging.warning(f"Error: {response.status_code}")
        return jsonify({data: "Error in svc1."})
    
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
    
@app.route('/viewlogs2')
def viewlogs2():
    with open('svc.log', 'r') as f:
        lines = f.readlines()
        last_15_lines = lines[-15:]
        return ''.join(last_15_lines)
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5002)
    logging.info(f"Server listening on localhost:5002")