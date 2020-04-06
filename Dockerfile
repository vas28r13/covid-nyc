# docker build -t covidnyc .
FROM python:3.8-slim

RUN mkdir -p /opt/scrpts
WORKDIR /opt/scripts

COPY ./requirements.txt /opt/scripts/

RUN pip install --no-cache-dir --upgrade pip && \
	pip install --no-cache-dir --requirement requirements.txt

COPY . /opt/scripts/

CMD python3.8 server.py