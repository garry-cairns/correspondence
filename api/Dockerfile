FROM ubuntu:14.04
MAINTAINER Garry Cairns
ENV REFRESHED_AT 2015-01-13

# update packages and prepare to build software
RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "build-essential", "vim", "git", "curl"]
RUN ["locale-gen", "en_GB.UTF-8"]

# install latest python
RUN ["apt-get", "-y", "build-dep", "python3-dev", "python3-imaging"]
RUN ["apt-get", "-y", "install", "python3-dev", "python3-imaging", "python3-pip"]

# prepare postgreSQL support
RUN ["apt-get", "-y", "build-dep", "python3-psycopg2"]

# create a python user to run our programs
RUN ["groupadd", "-r", "python"]
RUN ["useradd", "-r", "-g", "python", "python"]
WORKDIR /home/python
ADD ./ /home/python

# manage requirements
ENV ENQUIREMENTS_REFRESHED_AT 2015-01-14
RUN ["pip3", "install", "-r", "requirements.txt"]

# uncomment the line below to use container as a non-root user
# USER python:python
