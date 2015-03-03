FROM ubuntu:14.04
MAINTAINER Garry Cairns
ENV REFRESHED_AT 2015-02-11

# get the nginx package and set it up
RUN ["apt-get", "update"]
RUN ["apt-get", "-y", "install", "nginx"]

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log
VOLUME ["/var/cache/nginx"]
EXPOSE 80 443

# load nginx conf as root
ADD ./site.conf /etc/nginx/sites-available/correspondence
RUN ["ln", "-s", "/etc/nginx/sites-available/correspondence", "/etc/nginx/sites-enabled/correspondence"]
RUN ["rm", "-rf", "/etc/nginx/sites-available/default"]

# add application code as unprivileged user
RUN ["groupadd", "angular"]
RUN ["useradd", "angular", "-s", "/bin/bash", "-m", "-g", "angular", "-G", "angular"]
ENV HOME /home/angular
WORKDIR /home/angular
RUN ["chown", "-R", "angular:angular", "/home/angular"]
ADD ./dist/ /home/angular

#start the server
CMD ["nginx", "-g", "daemon off;"]
