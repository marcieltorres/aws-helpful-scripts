IMAGE_NAME=aws-helpful-scripts

.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

.PHONY: lint
lint: build
	docker run $(IMAGE_NAME) flake8 .

.PHONY: test
test:
	make -e ENV=TEST build