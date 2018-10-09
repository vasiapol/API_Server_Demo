# Kubernetes ready version of this project #
This project contains autoscalable version of the project which is using NGINX Ingress controller and k8s Metrics Server.
# Prerequisites

1. Kubernetes Metrics Server

https://github.com/kubernetes-incubator/metrics-server


2. NGINX Ingress Controller

https://github.com/kubernetes/ingress-nginx

Manifests to run this project in Kubenetes. Tested with Kubernetes v1.11.

### Deployment Steps
#### 1. Manual installation 
##### 1. Deploy API ###

```bash
$ kubectl apply -f API.yaml
```

##### 2. Deploy Horizontal Pod Autoscaler ###

```bash
$ kubectl apply -f ./ingress/api_hpa.yaml
```
##### 3. Deploy Ingress ###

```bash
$ kubectl apply -f ./ingress/ingress.yaml
```
#### 2.Installation using makefile if you already have prerequisites satisfied
Please refer to this [guide] (http://192.168.103.206:3000/Lv-335.DevOps/API_Server_Demo/src/Refactoring#deploy-in-kubernetes-cluster-using-makefile)