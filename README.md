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



As of my last knowledge update in September 2021, Jenkins doesn't have a built-in feature to directly export console output to Excel format. However, you can achieve this by using some Jenkins plugins in combination with other tools. Here's a general approach to achieve your requirement:

1. **Console Output to Text File:**
   - Use Jenkins plugins like "Log Parser Plugin" or "Copy Artifact Plugin" to save the console output of a build to a text file as part of your build process. These plugins allow you to save the console log to a file.

2. **Convert Text to Excel:**
   - After saving the console output as a text file, you can use external tools or scripts to convert this text file into an Excel format. You can use scripting languages like Python with libraries like Pandas or openpyxl to parse the text file and create an Excel file from it.

3. **Automate the Process:**
   - You can create a separate Jenkins job or a script that triggers after the main build job. This job/script will take the text file generated in step 1, convert it to Excel in step 2, and archive the Excel file.

4. **Optional Jenkins Plugins:**
   - There might be new Jenkins plugins available since my last update in September 2021. Check the Jenkins Plugin Index or the Jenkins community for any new plugins that offer direct Excel export capabilities from the console output.

Keep in mind that Jenkins and its plugin ecosystem are actively developed, so there may be new plugins or updates that provide more direct solutions to your specific use case. Be sure to check the Jenkins documentation and plugin repository for the most up-to-date information.

Remember to also consider the security implications of storing console output in Excel files, especially if these files contain sensitive information. Proper access controls and encryption should be considered if security is a concern.

Please verify if there have been any new developments or plugins introduced in Jenkins since my last update, as the Jenkins ecosystem is continuously evolving.
