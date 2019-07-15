FROM python:3.6-slim as builder

WORKDIR /app

ADD . .
RUN pip install pipenv
RUN pipenv install --system


FROM python:3.6-slim as builder-dev-packages

WORKDIR /app

COPY --from=builder /app .

RUN pip install pipenv
RUN pipenv install --dev
