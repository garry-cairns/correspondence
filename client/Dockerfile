FROM node:latest
MAINTAINER Garry Cairns
ENV REFRESHED_AT 2015-02-21

# now install our development environment
RUN ["npm", "install", "-g", "yo", "bower", "grunt-cli", "gulp"]
RUN ["npm", "install", "-g", "generator-ember"]

# create a non root user to run our programs
RUN ["groupadd", "-r", "ember"]
RUN ["useradd", "-r", "-g", "ember", "ember"]
ENV HOME /home/ember
ENV NODE_ENV development
WORKDIR /home/ember
ADD ./ /home/ember

# run programs as a non root user
USER ember:ember
