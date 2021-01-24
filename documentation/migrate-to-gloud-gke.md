# Migrate to Google Cloud GKE from local k8s

- Firstly, enable the container registery api from `Google Cloud Console`

- Configure Docker command-line tool to authenticate to Container Registery:

``gcloud auth configure-docker``

- Let the check them `gcloud container cluster` for `gcloud container clusters get-credentials cluster-1 --region europe-west6 --project enhanced-prism-233310`

```
arbade@Ardas-MacBook-Pro ~ % gcloud container clusters get-credentials cluster-1 --region europe-west6 --project enhanced-prism-233310
Fetching cluster endpoint and auth data.
kubeconfig entry generated for cluster-1.
```

- Tag the docker image and push to Google Cloud

``docker tag flask_service gcr.io/enhanced-prism-233310/flask_service``

```
rbade@Ardas-MacBook-Pro ~ %  docker push gcr.io/enhanced-prism-233310/flask_service 
The push refers to repository [gcr.io/enhanced-prism-233310/flask_service]
80d35d66a0fb: Pushed 
eff8fbf162dd: Pushed 
b375e1601f1c: Pushed 
c48ec05be700: Pushed 
dc1889a6560c: Pushed 
b7715857621b: Pushed 
7560054c4860: Pushed 
83743ed05e49: Pushed 
a9ffebc5be68: Pushed 
27d9a6169c9f: Pushed 
b9557a3d31d9: Pushed 
c8f52965417f: Pushed 
9cde96ca61c2: Pushed 
f3fd11fd6d6c: Pushed 
e553743c668b: Pushed 
88af765ea71f: Pushed 
b47c358499df: Pushed 
cbd550635f44: Pushed 
2efef025159b: Pushed 
3acbf6947195: Pushed 
f90fe4978ca2: Pushed 
88383b8e3cb5: Pushed 
e93627dfc607: Pushed 
8f23b00cc77f: Pushed 
cf691a2ea3f9: Pushed 
3d3e92e98337: Pushed 
8967306e673e: Pushed 
9794a3b3ed45: Pushed 
5f77a51ade6a: Pushed 
e40d297cf5f8: Pushed 
latest: digest: sha256:15c89483439e68c57404efe33a92be67e82caec70981298681e0bffd257e9d54 size: 6591

```

- Finally you would be able to see ``docker images``

```
arbade@Ardas-MacBook-Pro ~ % docker images 
REPOSITORY                                   TAG                 IMAGE ID            CREATED             SIZE
flask_service                                latest              fba7ca6e5e61        4 hours ago         954MB
gcr.io/enhanced-prism-233310/flask_service   latest              fba7ca6e5e61        4 hours ago         954MB

```