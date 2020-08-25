FROM pytorch/pytorch:1.5-cuda10.1-cudnn7-devel
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install libopencv-dev  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install --no-cache-dir numpy pillow

ENV HOME /home/
WORKDIR /home
