# Dockerfile

FROM python:3.10-slim-buster

RUN apt update \
    && apt-get -y install gcc libmariadb-dev \
    && apt install -y default-mysql-client \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install -U pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt