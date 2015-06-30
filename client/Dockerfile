FROM node:latest
MAINTAINER Garry Cairns
ENV REFRESHED_AT 2015-06-26

# install yeoman and other tools
RUN ["npm", "install", "-g", "yo"]
RUN ["npm", "install", "-g", "bower"]
RUN ["npm", "install", "-g", "grunt-cli"]
RUN ["npm", "install", "-g", "gulp"]
RUN ["npm", "install", "-g", "generator-karma", "generator-angular"]

# add application code as unprivileged user
RUN ["groupadd", "angular"]
RUN ["useradd", "angular", "-s", "/bin/bash", "-m", "-g", "angular", "-G", "angular"]
ENV HOME /home/angular
WORKDIR /home/angular
RUN ["chown", "-R", "angular:angular", "/home/angular"]
USER angular:angular
