FROM python:3.6-slim

ARG ENV=DEV

WORKDIR /app

ADD . .
RUN pip install pipenv
RUN pipenv install