88# ansible-webhook

```
docker run -v /etc/ansible:/ansible -it --entrypoint="" hackcoderr/ansible-webhook:v1.0.0 ls /ansible
```

```
curl -X POST http://127.0.0.1:5001/send
```
```
curl -X POST -H "Content-Type: application/json" -d '{"pod_name": "YourPodName", "cluster_name": "YourClusterName"}' http://127.0.0.1:5000/send
```


Here's a Python script that reads a text file, processes its contents, and saves the data in an Excel file:
```
import openpyxl

# Read the text file
with open('console_output.txt', 'r') as file:
    lines = file.readlines()

# Create a new Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Write the text lines to Excel rows
for i, line in enumerate(lines):
    worksheet.cell(row=i+1, column=1, value=line.strip())

# Save the Excel file
workbook.save('console_output.xlsx')
```

```
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the path to the file where you want to store the alert data
alert_data_file = 'alert_data.txt'

@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json  # Parse incoming JSON data

    # Write the alert data to the specified file (overwriting existing data)
    with open(alert_data_file, 'w') as file:
        file.write(str(data) + '\n')

    return jsonify({'message': 'Alert received and stored successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

```
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the path to the file where you want to store the alert data
alert_data_file = 'alert_data.txt'

@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json  # Parse incoming JSON data

    # Check if the status of the alert is not "resolved" before saving
    if data['status'] != 'resolved':
        # Extract 'k8sname' and 'pod' fields from the alert and save them to a dictionary
        alert_info = {
            'k8sname': data['commonLabels']['k8sname'],
            'pod': data['commonLabels']['pod']
        }

        # Write the extracted alert info to the specified file
        with open(alert_data_file, 'w') as file:
            file.write(str(alert_info) + '\n')

    return jsonify({'message': 'Alert received and stored successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```

Create a Jenkinsfile:

Create a Jenkinsfile and define the pipeline stages. You can create a new file named Jenkinsfile in your project's root directory or wherever your Jenkins job workspace is located. Here's a basic example of a Jenkinsfile for your task:



```

import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the path to the Python file where you want to store the alert data
alert_data_file = 'alert_data.py'

@app.route('/alert', methods=['POST'])
def receive_alert():
    data = request.json  # Parse incoming JSON data

    # Check if the status of the alert is not "resolved" before saving
    if data['status'] != 'resolved':
        # Extract 'k8sname' and 'pod' fields from the alert
        k8sname = data['commonLabels']['k8sname']
        podname = data['commonLabels']['pod']

        # Write the extracted alert info to the specified Python file
        with open(alert_data_file, 'w') as file:
            file.write(f'k8sname = "{k8sname}"\n')
            file.write(f'Podname = "{podname}"\n')

        # Trigger the execution of demo.py
        subprocess.run(['python', 'demo.py'])

    return jsonify({'message': 'Alert received and stored successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
