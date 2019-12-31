FROM python:2.7

WORKDIR app
COPY requirement.txt /app
RUN apt-get update && apt-get update \
    && pip install -r requirement.txt
