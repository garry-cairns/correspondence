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

# load nginx conf
ADD ./site.conf /etc/nginx/sites-available/correspondence
RUN ["ln", "-s", "/etc/nginx/sites-available/correspondence", "/etc/nginx/sites-enabled/correspondence"]

CMD ["nginx", "-g", "daemon off;"]
