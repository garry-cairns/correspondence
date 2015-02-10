FROM nginx
MAINTAINER Garry Cairns
ENV REFRESHED_AT 2015-02-10

# load nginx conf
ADD ./site.conf /etc/nginx/sites-available/correspondence
RUN ["mkdir", "/etc/nginx/sites-enabled/"]
RUN ["ln", "-s", "/etc/nginx/sites-available/correspondence", "/etc/nginx/sites-enabled/correspondence"]
