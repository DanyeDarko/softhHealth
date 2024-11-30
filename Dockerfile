FROM python:3.7.9-slim-stretch as base
WORKDIR /dependencies
RUN pip install --no-warn-script-location \
   --prefix=/dependencies esptool adafruit-ampy

FROM python:3.7.9-slim-stretch as prod 
RUN apt-get update && apt-get install -y \
     picocom \
    && rm -rf /var/lib/apt/lists/*
COPY --from=base /dependencies /usr/local
COPY esp8266menu.sh .


