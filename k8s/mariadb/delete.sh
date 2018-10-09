#!/bin/bash


kubectl delete -f etcd-cluster.yml
#kubectl delete -f mariadb-rs.yml
kubectl delete -f mariadb-pvc.yml
kubectl delete -f mariadb-pv.yml
kubectl delete -f mariadb-ss.yml
