FROM python:latest

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt