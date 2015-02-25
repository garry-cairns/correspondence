FROM ubuntu:14.04
MAINTAINER Garry Cairns
ENV REFRESHED_AT 2015-02-21

# make sure packages are up-to-date
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN ["apt-get", "-y", "update"]

# install python software properties in order to add a repository
RUN ["apt-get", "-yq", "install", "python-software-properties", "software-properties-common"]

# install utilities
RUN ["apt-get", "-y", "install", "vim", "git", "zip", "bzip2", "fontconfig", "curl"]

# nodejs from PPA
RUN ["add-apt-repository", "ppa:chris-lea/node.js"]
RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "nodejs"]

# install yeoman and its toolchain
RUN ["npm", "install", "-g", "yo", "bower", "grunt-cli", "gulp"]

# configure ember and root users
# RUN ["echo", "'root:ember'", "|", "chpasswd"]
RUN ["groupadd", "ember"]
RUN ["useradd", "ember", "-s", "/bin/bash", "-m", "-g", "ember", "-G", "ember"]
# RUN ["echo", "'ember:ember'", "|", "chpasswd"]

# move into our working directory
# ADD must be after chown see http://stackoverflow.com/a/26145444/1281947
ENV HOME /home/ember
WORKDIR /home/ember
RUN ["chown", "-R", "ember:ember", "/usr/lib/nodejs"]
RUN ["chown", "-R", "ember:ember", "/usr/lib/node_modules"]
RUN ["chown", "-R", "ember:ember", "/home/ember"]
ADD ./ /home/ember

# now install our development environment
RUN ["npm", "install", "-g", "generator-ember"]

# run programs as a non root user
USER ember

# expose grunt port
EXPOSE 9000
EXPOSE 35729
