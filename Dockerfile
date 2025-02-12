FROM ubuntu:22.04

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ARG USER_ID=1000
ARG GROUP_ID=1000

RUN if getent group clima ; then groupdel clima; fi
RUN groupadd -g ${GROUP_ID} clima
RUN useradd -l -u ${USER_ID} -g clima clima
RUN install -d -m 0775 -o clima -g clima /home/clima

RUN apt update -y && apt upgrade -y
RUN apt-get install -y software-properties-common python3.10 python3-pip
RUN pip3 install Flask geojson psycopg2-binary Flask-Cors python-dotenv pipenv virtualenv virtualenv-clone
RUN pip3 install uwsgi
RUN pip3 install requests

USER clima
