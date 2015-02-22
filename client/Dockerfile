FROM ubuntu:14.04
MAINTAINER Garry Cairns
ENV REFRESHED_AT 2015-02-21

# get npm
RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "build-essential"]
RUN ["apt-get", "-y", "install", "nodejs"]
RUN ["apt-get", "-y", "install", "npm"]
RUN ["npm", "install", "-g", "npm"]

# make a soft link from nodejs to node to avoid naming problems
RUN ["ln", "-s", "/usr/bin/nodejs", "/usr/bin/node"]

# now install our development environment
RUN ["npm", "install", "-g", "yo", "bower", "grunt-cli", "gulp"]
RUN ["npm", "install", "-g", "generator-ember"]

# append to PATH variable
RUN echo '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bash_profile

# create a non root user to run our programs
RUN ["groupadd", "-r", "ember"]
RUN ["useradd", "-r", "-g", "ember", "ember"]
ENV HOME /home/ember
WORKDIR /home/ember
ADD ./ /home/ember

# run programs as a non root user
USER ember:ember
