uniq:= $(shell uuidgen)
tag = $(shell whoami)-dev-$(uniq)

.PHONY: k8s_deploy
k8s_deploy: docker_image_build registry_push build_manifest kube_deploy rebuild_example_manifest

.PHONY: docker_image_build
docker_image_build:
	docker build --tag $(name) .
	docker tag $(name):latest polianskiyvasyl/$(project)-$(name):$(tag)

.PHONY: build_manifest
build_manifest:
	sed -i "s|__IMAGE__|polianskiyvasyl/$(project)-$(name):$(tag)|g" API_example.yml
	sed -i "s|__NAME__|$(name)|g"  API_example.yml

.PHONY: registry_push
registry_push:
	docker push polianskiyvasyl/$(project)-$(name):$(tag)

.PHONY: kube_deploy
kube_deploy:
	kubectl apply -f API_example.yml

.PHONY: rebuild_example_manifest
rebuild_example_manifest:
	sed -i "s|polianskiyvasyl/$(project)-$(name):$(tag)|__IMAGE__|g" API_example.yml
	sed -i "s| $(name)| __NAME__|g"  API_example.yml

~
~
~
~
~
~
