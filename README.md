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
