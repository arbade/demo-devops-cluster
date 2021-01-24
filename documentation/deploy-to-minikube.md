# Deploying k8s cluster the application

- Firstly, we need to start minikube

    ``minikube start``

- We need to create service & deployment yaml for ``kubectl`` config 

```yaml
# flaskservice_deployment.yml
apiVersion: apps/v1 # for versions before 1.9.0 use apps/v1beta2
kind: Deployment
metadata:
  name: hello-flask
spec:
  selector:
    matchLabels:
      app: hello-flask
  replicas: 2 # tells deployment to run 2 pods matching the template
  template:
    metadata:
      labels:
        app: hello-flask
    spec:
      containers:
      - name: hello-flask
        image: flask_service
        imagePullPolicy: Never
        ports:
        - containerPort: 8083
```
```yaml
# 2_service.yml
apiVersion: v1
kind: Service
metadata:
  name: hello-flask
spec:
  selector:
    app: hello-flask
  type: NodePort
  ports:
    - name: http
      port: 80
      targetPort: 80
```

- After the creation, we need to apply yml config into kubectl 

``kubectl apply -f flaskservice_deployment.yml`` 
``kubectl apply -f 2_service.yml``
