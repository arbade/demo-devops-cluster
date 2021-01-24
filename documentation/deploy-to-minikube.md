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

-Then, we need to create pods & services
``kubectl create -f flaskservice_deployment.yml``

``kubectl create -f 2_service.yml``

- Finally, it would be able to see `service` & `pods` 
```
arbade@Ardas-MacBook-Pro ~ % kubectl get svc
NAME          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
hello-flask   NodePort    10.109.106.207   <none>        80:32420/TCP   11h
kubernetes    ClusterIP   10.96.0.1        <none>        443/TCP        12h
arbade@Ardas-MacBook-Pro ~ % kubectl get all
NAME                               READY   STATUS    RESTARTS   AGE
pod/hello-flask-7489c56888-gnq8d   1/1     Running   1          11h
pod/hello-flask-7489c56888-hwthw   1/1     Running   1          11h

NAME                  TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/hello-flask   NodePort    10.109.106.207   <none>        80:32420/TCP   11h
service/kubernetes    ClusterIP   10.96.0.1        <none>        443/TCP        12h

NAME                          READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/hello-flask   2/2     2            2           11h

NAME                                     DESIRED   CURRENT   READY   AGE
replicaset.apps/hello-flask-7489c56888   2         2         2       11h

```

- Another way to able to see cluster information : ``minikube dashboard``

