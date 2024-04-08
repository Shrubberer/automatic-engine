from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LAB_URL = "http://el-vote-app-cbc-prod.apps.swtd-ocp4.unilab"  # target 

@app.route('/', methods=['POST'])
def webhook():
    # Forward the GitHub webhook payload to the lab address
    headers = {'Content-Type': 'application/json'}
    response = requests.post(LAB_URL, headers=headers, json=request.json)

    if response.ok:
        return jsonify({"status": "success", "message": "Webhook forwarded successfully to lab"})
    else:
        return jsonify({"status": "error", "message": "Failed to forward webhook to lab"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
