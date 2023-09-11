# ansible-webhook

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





Create a Jenkinsfile:

Create a Jenkinsfile and define the pipeline stages. You can create a new file named Jenkinsfile in your project's root directory or wherever your Jenkins job workspace is located. Here's a basic example of a Jenkinsfile for your task:





