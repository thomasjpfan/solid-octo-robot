.PHONY: build

build: export REGISTRY ?= lcoalhost:30000
build: export TAG ?= dev
build:
	docker image build -f Dockerfile --platform linux/amd64 -t ${REGISTRY}/us-migration:${TAG} .
