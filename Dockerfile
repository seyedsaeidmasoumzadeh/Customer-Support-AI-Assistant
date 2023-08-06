FROM python:3.8.17-slim

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PIP_DISABLE_PIP_VERSION_CHECK=TRUE
ENV TOKENIZERS_PARALLELISM=TRUE

RUN apt-get update && apt-get install -y \
    build-essential

RUN pip install --upgrade pip setuptools

RUN useradd -ms /bin/bash seyed
WORKDIR /home/code


COPY requirements.txt /home/code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/code/

ENV HOME /home
ENV PATH="/home/.local/bin:${PATH}"
ENV PYTHONPATH /home/code/src
RUN chown -R seyed /home/code

RUN mkdir -p /home/.local
RUN mkdir -p /home/.cache

RUN chmod -R 777 /home/.local
RUN chmod -R 777 /home/.cache


# nltk download
RUN mkdir /home/nltk_data
RUN chmod 777 /home/nltk_data

USER seyed