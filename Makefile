IMAGE_NAME=aws-helpful-scripts

.PHONY: build
build:
	docker build --target builder -t $(IMAGE_NAME) .

build/dev:
	docker build --target builder-dev-packages -t $(IMAGE_NAME) .

.PHONY: lint
lint: build/dev
	docker run $(IMAGE_NAME) pipenv run flake8
