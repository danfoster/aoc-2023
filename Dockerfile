FROM python:3.12
RUN apt-get update && apt-get install -y \
    patchelf \
    hyperfine \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /
RUN pip install -r /requirements.txt
