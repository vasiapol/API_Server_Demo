#!/bin/bash

kubectl create -f etcd-cluster.yml
kubectl create -f mariadb-pv.yml
kubectl create -f mariadb-pvc.yml
kubectl create -f mariadb-ss.yml
