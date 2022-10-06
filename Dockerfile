FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir djangoTestTask
WORKDIR /djangoTestTask
COPY ./djangoTestTask /djangoTestTask

RUN adduser -D user

USER user
