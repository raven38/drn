FROM pytorch/pytorch:1.2-cuda10.0-cudnn7-devel
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update && apt-get -y install libopencv-dev  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install --no-cache-dir numpy pillow

ENV HOME /home/
WORKDIR /home
