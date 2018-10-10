#!/bin/bash
kubectl delete -f serviceaccount.yaml
sleep 3
# kubectl delete -f ingress-grafana.yaml
# sleep 3
kubectl delete -f nms.yaml
sleep 3
kubectl delete -f ingress.yaml
