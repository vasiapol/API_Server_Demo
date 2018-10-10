# Kubernetes ready version of this project #
This project contains autoscalable version of the project which is using NGINX Ingress controller and k8s Metrics Server.
## Prerequisites

#### 1. Kubernetes Metrics Server

   - Metrics Server is a cluster-wide aggregator of resource usage data.

   - Metric server collects metrics from the Summary API, exposed by Kubelet on each node.

   - Metrics Server registered in the main API server through Kubernetes aggregator, which was introduced in Kubernetes

`https://github.com/kubernetes-incubator/metrics-server`


#### 2. NGINX Ingress Controller Setup
This repository contains the NGINX controller built around the Kubernetes Ingress resource that uses ConfigMap to store the NGINX configuration. Tested with Kubernetes v1.11.
 1.Clone this repo:

 `git clone http://192.168.103.206:3000/Lv-335.DevOps/API_Server_Demo.git`

 2.Create namespace ingress-nginx:

  `kubectl apply -f nms.yaml`
 3. Create config-map:

 `kubectl apply -f config-map.yaml`
 4. Create Clusterrolebinding and serviceaccount:

 `kubectl apply -f serviceaccount.yaml`  

 5. Deploy NGINX ingress controller:

 `kubectl apply -f nginx-ingress-controller.yaml`

 6. Create service nodeport:

  `kubectl apply -f service-nodeport.yaml`

 7. Create ingress rules for appliccation:

  `kubectl apply -f ingress.yaml`

 8. Edit and apply Horizontal pod Autoscaler:

 `kubectl apply -f api_hpa.yaml`     

 - #### Quick deployment Ingress Controller script:
  `./deploy.sh`
 - #### Uninstall the Ingress Controller
  `./delete.sh`


### Deployment Steps
#### I. Manual installation
##### 1. Deploy API ###


`kubectl apply -f API.yaml`


#### II.Installation using makefile if you already have prerequisites satisfied
Please refer to this [guide] ``(http://192.168.103.206:3000/Lv-335.DevOps/API_Server_Demo/src/Refactoring#deploy-in-kubernetes-cluster-using-makefile)``
