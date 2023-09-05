from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def receive_alert():
    data = request.json  # Assuming that AlertManager sends alerts as JSON
    pod_name = data.get('pod_name')
    cluster_name = data.get('cluster_name')

    # Append pod_name and cluster_name to a file
    with open('alerts.txt', 'a') as f:
        f.write(f"Pod: {pod_name}, K8s Cluster: {cluster_name}\n")

    return jsonify({'message': 'Alert received and processed successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
