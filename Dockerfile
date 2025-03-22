# xhost +local:
# docker build --no-cache -t graphabc-test-env .
# docker run -v ./graphabc:/build/graphabc -v $HOME/.Xauthority:/home/nonroot/.Xauthority -e DISPLAY=$DISPLAY --pid=host -v /tmp/.X11-unix:/tmp/.X11-unix:ro -it graphabc-test-env bash

#  https://hub.docker.com/_/python/
#  https://github.com/python/cpython/tags
#FROM python:3.14.0a5-bookworm
#FROM python:3.13.2-bookworm
#FROM python:3.12.9-bookworm
#FROM python:3.12.7-bookworm
FROM python:3.12.0-bookworm
#FROM python:3.11.11-bookworm
#FROM python:3.11.7-bookworm
#FROM python:3.10.16-bookworm
#FROM python:3.9.21-bookworm

RUN apt-get update
RUN apt-get install -y \
  git vim bash sudo build-essential m4 pkgconf jq
RUN useradd -U -m nonroot

RUN echo "nonroot ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/nonroot && chmod 0440 /etc/sudoers.d/nonroot

RUN mkdir /build
ADD ./test /build/graphabc-test
RUN chown -R nonroot:nonroot /build

USER nonroot

RUN sudo apt install -y x11-apps xauth
RUN sudo apt install -y libgl1-mesa-glx

WORKDIR /build/graphabc-test
RUN pip install --upgrade pip
RUN pip install raylib

RUN echo "alias ls='ls --color=auto'" >> ~/.bashrc
RUN echo "alias ll='ls -AlhFv'" >> ~/.bashrc
