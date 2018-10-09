# API on Kubernetes #
# Prerequisites

1. Kubernetes Metrics Server

2. NGINX Ingress Controller


Manifests to run this project in Kubenetes. Tested with Kubernetes v1.11.

## Deployment Steps ##

### 1. Deploy API ###

```bash
$ kubectl apply -f API.yaml
```

### 2. Deploy Horizontal Pod Autoscaler ###

```bash
$ kubectl apply -f ./ingress/api_hpa.yaml
```
### 3. Deploy Ingress ###

```bash
$ kubectl apply -f ./ingress/ingress.yaml
```
