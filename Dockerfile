FROM python:3.7.9-slim-stretch as build
RUN pip install --upgrade pip  && \
    pip install --upgrade esptool 

FROM python:3.7.9-slim-stretch as prod 
COPY esp8266menu.sh .
RUN apt-get update && apt-get install -y \
     picocom \
    && rm -rf /var/lib/apt/lists/*
ENTRYPOINT [ "./esp8266menu.sh" ]
