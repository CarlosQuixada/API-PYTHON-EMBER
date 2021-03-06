FROM ubuntu:16.04

MAINTAINER Carlos Quixadá

RUN apt-get update && \
        apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -y

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && \
        apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

COPY requirements.txt requirements.txt
RUN pip3.6 install -r requirements.txt

COPY . .

RUN mkdir logs

RUN python3.6 -m nltk.downloader wordnet pros_cons reuters stopwords rslp punkt


ENTRYPOINT ["/docker-entrypoint.sh"]
