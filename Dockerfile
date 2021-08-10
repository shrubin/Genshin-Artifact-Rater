FROM python:3.8-slim-buster

WORKDIR /app

ENV FLASK_APP=bot.py


RUN apt-get update -y && apt-get install -y htop libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender-dev python3-pip python-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


RUN groupadd --gid 1000 lisa
RUN useradd --uid 1000 --gid lisa --shell /bin/bash --create-home lisa

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
RUN usermod -u $UID lisa
RUN groupmod -g $GID lisa

USER lisa


COPY . /app


CMD [ "python3", "bot.py"]
