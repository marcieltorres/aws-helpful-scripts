# AWS helpful scripts
The `AWS helpful scripts` is a CLI (*Command Line Interface*) with helpful commands to help some people to manage some stuff in the `AWS Cloud`, like this:

- it helps to start/stop `EC2` instances
- it helps to start/stop `RDS` instances
- and more (soon) 


### Built with
- [Python 3.6](https://www.python.org/downloads/release/python-365/)
- [Pipenv](https://docs.pipenv.org/en/latest/)
- [Boto3](https://github.com/boto/boto3)
- [Argparse](https://docs.python.org/3/library/argparse.html)


### How to install locally

To configure local it's necessary to install [Python 3.6](https://www.python.org/downloads/release/python-365/) and  [Pipenv](https://docs.pipenv.org/en/latest/). But it's unnecessary because you can run the whole project using **Docker** with the available commands in the `Makefile`. We are using [multistage-build](https://docs.docker.com/develop/develop-images/multistage-build/) to build the project image.

## How to build

```bash
make build
```

## How to build an image with the dev packages

```bash
make build/dev
```

## How to test

```bash
make test
```

## Using lint

```bash
make lint
```