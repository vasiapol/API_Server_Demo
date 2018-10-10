#!/bin/bash
kubectl apply -f nms.yaml
sleep 3
kubectl apply -f config-map.yaml
sleep 3
kubectl apply -f serviceaccount.yaml
sleep 3
kubectl apply -f service-nodeport.yaml
sleep 3
kubectl apply -f nginx-ingress-controller.yaml
sleep 3
kubectl apply -f ingress.yaml
# sleep 3
# kubectl apply -f ingress-grafana.yaml
