FROM python:3.11
RUN apt-get update && apt-get install -y \
    patchelf \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /
RUN pip install -r /requirements.txt
