VERSION  := $(shell git describe --tags --always --dirty)

# define image names
REGISTRY := {{cookiecutter.dockerhub_registry}}
APP      := {{cookiecutter.project_name}}

# build tags
IMG           := $(REGISTRY)/$(APP)
IMG_VERSIONED := $(IMG):$(VERSION)
IMG_LATEST    := $(IMG):latest

.PHONY: push build tag

push: build tag
	docker push $(IMG_VERSIONED)
	docker push $(IMG_LATEST)

build:
	docker buildx build --platform linux/amd64 -t $(IMG_VERSIONED) . || \
	docker build -t $(IMG_VERSIONED) .

tag:
	docker tag $(IMG_VERSIONED) $(IMG_LATEST)

