FROM pypy:3.10
RUN apt-get update && apt-get install -y \
    patchelf \
    hyperfine \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /
RUN pip install -r /requirements.txt
