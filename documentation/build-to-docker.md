# Build to DockerFile & Dockerize the App

Before start to developing our service we need to install packages and dependencies.

First of all, installation the python, pip (*Python Package Manager*), git and docker.Finally, we would be able to use pip to install the virtual environment

```
pip install virtualenv
```

#### Set up the project

- Make a new empty directory flask_service
- Set up a virtual enviroment in a directory called venv with the command ``virtualenv env``
- Active the virtual enviroment with ``flask_service/venv/bin/active``
- Make a file requirements.txt that has all your dependencies in it. For the simplest flask app we need only

```text
Flask==1.1.2
```

- Install your dependencies with `pip install -r requirements.txt```

- It would be able to see at the below line:
```
arbade@Ardas-MacBook-Pro demo % mkdir flask_service
arbade@Ardas-MacBook-Pro demo % cd flask_service/
arbade@Ardas-MacBook-Pro flask_service % virtualenv venv
arbade@Ardas-MacBook-Pro flask_service % echo "Flask==1.1.2" >> requirements.txt
arbade@Ardas-MacBook-Pro flask_service % cat requirements.txt
Flask==1.1.2

arbade@Ardas-MacBook-Pro flask_service % source venv/bin/activate
(venv) arbade@Ardas-MacBook-Pro flask_service % pip3 install -r requirements.txt
Collecting Flask==1.1.2
  Using cached Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting click>=5.1
  Using cached click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting itsdangerous>=0.24
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2>=2.10.1
  Using cached Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting MarkupSafe>=0.23
  Using cached MarkupSafe-1.1.1-cp38-cp38-macosx_10_9_x86_64.whl (16 kB)
Collecting Werkzeug>=0.15
  Using cached Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, Flask
Successfully installed Flask-1.1.2 Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 itsdangerous-1.1.0


```

#### Code the endpoint

- Make a flask app at `app/main.py`

```
(venv) arbade@Ardas-MacBook-Pro flask_service % mkdir app
(venv) arbade@Ardas-MacBook-Pro flask_service % touch app/main.py
```

```
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    result='Welcome to my app'
    return jsonify(result),200


@app.route("/status")
def other():
    result2=''
    return jsonify(result2),204
```
- when we call ip/codes it will return codes

#### Make the DockerFile

- A Dockerfile is a file called ``Dockerfile` (with no extension ) which tells Docker how to build an image.

- Directory should be like this:
```
.
├── app
│   └── main.py
└── Dockerfile
└── requirements.txt
```

```dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6

# copy over our requirements.txt file
COPY requirements.txt /tmp/

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# copy over our app code
COPY ./app /app
```

#### Building Docker Image for -docker build

`docker build -t flask_service .`

```
(venv) arbade@Ardas-MacBook-Pro flask_service % docker build -t flask_service .
Sending build context to Docker daemon  14.43MB
Step 1/5 : FROM tiangolo/uwsgi-nginx-flask:python3.6
python3.6: Pulling from tiangolo/uwsgi-nginx-flask
90fe46dd8199: Pull complete 
35a4f1977689: Pull complete 
bbc37f14aded: Pull complete 
74e27dc593d4: Pull complete 
4352dcff7819: Pull complete 
1847e662e737: Pull complete 
11d40aa4a4d0: Pull complete 
423a225c2f8b: Pull complete 
730abf0e8db7: Pull complete 
2f2c1f99caec: Pull complete 
117b2bb6b9f5: Pull complete 
24cf85cbbf19: Pull complete 
e5b1d4c157be: Pull complete 
41ed8631c488: Pull complete 
4cea017a23a1: Pull complete 
634fcb400bb1: Pull complete 
751c69d0afb6: Pull complete 
d5a08367e03a: Pull complete 
d9cd7fb23581: Pull complete 
f81f7e2c0189: Pull complete 
cd58b8e863a0: Pull complete 
bc088c01951c: Pull complete 
2a8e3800133d: Pull complete 
31917b7ecee1: Pull complete 
8209ceb7fced: Pull complete 
24e83c1bdaaa: Pull complete 
Digest: sha256:98c838b9d7861245ca4035816e8deb0f4efa11bc5deb8bdd74df0ec0b2aa5836
Status: Downloaded newer image for tiangolo/uwsgi-nginx-flask:python3.6
 ---> 997d8bb5f569
Step 2/5 : COPY requirements.txt /tmp/
 ---> 60795a46d052
Step 3/5 : RUN pip install -U pip
 ---> Running in 143b2e44ae72
Collecting pip
  Downloading pip-21.0-py3-none-any.whl (1.5 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.1
    Uninstalling pip-20.1:
      Successfully uninstalled pip-20.1
Successfully installed pip-21.0
Removing intermediate container 143b2e44ae72
 ---> 9e07f9b1b3c4
Step 4/5 : RUN pip install -r /tmp/requirements.txt
 ---> Running in f2959a9238e5
Requirement already satisfied: Flask==1.1.2 in /usr/local/lib/python3.6/site-packages (from -r /tmp/requirements.txt (line 1)) (1.1.2)
Requirement already satisfied: itsdangerous>=0.24 in /usr/local/lib/python3.6/site-packages (from Flask==1.1.2->-r /tmp/requirements.txt (line 1)) (1.1.0)
Requirement already satisfied: Werkzeug>=0.15 in /usr/local/lib/python3.6/site-packages (from Flask==1.1.2->-r /tmp/requirements.txt (line 1)) (1.0.1)
Requirement already satisfied: Jinja2>=2.10.1 in /usr/local/lib/python3.6/site-packages (from Flask==1.1.2->-r /tmp/requirements.txt (line 1)) (2.11.2)
Requirement already satisfied: click>=5.1 in /usr/local/lib/python3.6/site-packages (from Flask==1.1.2->-r /tmp/requirements.txt (line 1)) (7.1.2)
Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.6/site-packages (from Jinja2>=2.10.1->Flask==1.1.2->-r /tmp/requirements.txt (line 1)) (1.1.1)
Removing intermediate container f2959a9238e5
 ---> 5ab67e6b0d28
Step 5/5 : COPY ./app /app
 ---> fba7ca6e5e61
Successfully built fba7ca6e5e61
Successfully tagged flask_service:latest
```
This tells Docker to build a container using the project in the present working directory (the ``.` at the end), and tag it ``flask_service`` ( `` -t `` stands for “tag”). Docker will pull down the base image `tiangolo/uwsgi-nginx-flask:flask`` from Docker Hub, then copy our app code into the container.

we can check docker image by ``docker images ``

```
(venv) arbade@Ardas-MacBook-Pro flask_service % docker images
REPOSITORY                    TAG                 IMAGE ID            CREATED             SIZE
flask_service                 latest              fba7ca6e5e61        6 seconds ago       954MB

```