uniq:=$(shell uuidgen)
tag = $(shell whoami)-dev-$(uniq)

#.PHONY: k8s_deploy
#k8s_deploy: create_namespace env_secret docker_image_build registry_push build_manifest kube_deploy get_exposed_ip

.PHONY: docker_image_build
docker_image_build:
        docker build --tag $(name) .
        docker tag $(name):latest polianskiyvasyl/$(project)/$(name):$(tag)

.PHONY: build_manifest
build_manifest:
        cat APi.yml | sed s/__IMAGE__/polianskiyvasyl/$(progect)$(name):$(tag)/g | sed s/__NAME__/$(name)/g > API.yml

.PHONY: registry_push
registry_push:
        docker -- push polianskiyvasyl/$(project)/$(name):$(tag)

.PHONY: kube_deploy
kube_deploy:
        kubectl apply -f API.yml

