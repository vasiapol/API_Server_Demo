uniq:=$(shell uuidgen)
tag = $(shell whoami)-dev-$(uniq)

.PHONY: k8s_deploy
k8s_deploy: docker_image_build registry_push build_manifest kube_deploy

.PHONY: docker_image_build
docker_image_build:
        docker build --tag $(name) .
        docker tag $(name):latest polianskiyvasyl/$(name):$(tag)

.PHONY: build_manifest
build_manifest:
        sed -i "s|__IMAGE__|polianskiyvasyl/$(name):$(tag)|g" k8s_API.yml
        sed -i "s|__NAME__|$(name)|g"  k8s_API.yml

.PHONY: registry_push
registry_push:
        docker push polianskiyvasyl/$(name):$(tag)

.PHONY: kube_deploy
kube_deploy:
        kubectl apply -f k8s_API.yml

~
~
~
~
~
~
