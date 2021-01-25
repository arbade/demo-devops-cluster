# demo-devops-cluster
[![pypi supported versions](https://img.shields.io/pypi/pyversions/kubernetes.svg)](https://pypi.python.org/pypi/kubernetes)
[![Docker Hub](https://img.shields.io/badge/Docker-Hub-blue.svg)](https://hub.docker.com/r/bludit/docker/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployment-blue.svg)](https://github.com/bludit/docker/tree/master/kubernetes)

## Description
Python training, local Docker &amp; Kubernetes files, Google Cloud GKE configs

## Pre-Reqiurements
- Docker 19.03.13
- Minikube v1.15.0
- Pip 20.1
- Python 3.8
- Virtualenv 20.4.0
- Flask 1.1.2
- Google Cloud 


## Installation
From source:
```
git clone https://github.com/arbade/demo-devops-cluster.git
```
From web:
* brew for macOS
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
* minikube for macOS
```
brew install minikube
```
* docker for macOS
```
brew cask install docker
```
* pip for macOS
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

#now execute the downloaded file using below command

python3 get-pip.py
```
* python3 for macos
```
brew install python3
```
* virtualenv for macOS
```
pip install virtualenv
```
* flask for python on macOS
```
pip install python
```
## Table of Content to Endpoints
* For local

* * Basic Flask Application

| Method                  | Content           | Response       |
|-------------------------|-------------------|----------------|
| http://127.0.0.1:5000/  | Welcome to my app | 200 OK         |
| http://127.0.0.1:5000/status |                   | 204 No Content |
|                         |                   |                |

* * For local docker

| Method                     | Content           | Response       |
|----------------------------|-------------------|----------------|
| http://localhost:80/       | Welcome to my app | 200 OK         |
| http://localhost:80/status |                   | 204 No Content |
|                            |                   |                |

* * For local minikube (k8s)

| URL                            | Content           | Response       |
|--------------------------------|-------------------|----------------|
| http://127.0.0.1:63853/        | Welcome to my app | 200 OK         |
| http://127.0.0.1:63853/status  |                   | 204 No Content |
|                                |                   |                |

* For Cloud

* * Google Kubernetes Engine (GKE)

| URL                            | Content           | Response       |
|--------------------------------|-------------------|----------------|
| 34.65.221.236:5000             | Welcome to my app | 200 OK         |
| 34.65.221.236:5000/status      |                   | 204 No Content |
|                                |                   |                |

* * Mysql Server

| Connection IP | Connection Name                                 |
|---------------|-------------------------------------------------|
| 34.65.145.206 | enhanced-prism-233310:europe-west6:mysql-server |
|               |                                                 |


## Solution RoadMap

It could be following links for deployment related flask app

- Build to dockerfile python applicaton [`build dockerfile`](documentation/build-to-docker.md)
- Deploy the docker file on minikube [`deploy on minikube`](documentation/deploy-to-minikube.md)
- Migrate to Google Cloud GKE to k8s  Deploy the docker file on minikube [`migrate local pods`](documentation/migrate-to-gloud-gke.md)

