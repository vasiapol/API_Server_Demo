# MariaDB Galera on Kubernetes #

YAML definitions to run MariaDB Galera Cluster 10.1 on Kubernetes. Tested on Kubernetes v1.11 using  StatefulSet.

## Deployment Steps ##

### 1. Deploy an etcd cluster ###

The image requires an etcd (standalone or cluster) for service discovery. Deploy an etcd cluster with Pods and Services:

```bash
$ kubectl create -f etcd-cluster.yaml
```

### 2. Deploy the Galera Cluster ###

**StatefulSet**

First of all you need to create persistentvolume and persistentvolumeclaim.

```bash
$ kubectl create -f mariadb-pv.yml
$ kubectl create -f mariadb-pvc.yml
```

### 3.Then, deploy the Galera Cluster pods:

```bash
$ kubectl create -f mariadb-ss.yml
```

