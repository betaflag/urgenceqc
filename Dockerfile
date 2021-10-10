FROM python:3.9.7-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update -y && apt-get install -y default-libmysqlclient-dev build-essential

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

CMD gunicorn urgenceqc.wsgi
