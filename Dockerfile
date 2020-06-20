# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.8
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
COPY . /usr/src/app