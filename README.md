# Correspondence

A web service to produce business correspondence.

LICENSE: BSD

## Getting up and running

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* Docker
* docker-compose

Open a terminal at the project root and type::

    $ sudo docker-compose build

You can now run the ``docker-compose up`` command::

    $ sudo docker-compose up

This will build your database, api and webserver, and link them to each other.

## API layer

The API is the meat of this project. It is expected you will want to integrate with or develop your own client. Please see the README in the `api` folder for its documentation.

## Demo client

The webserver directory contains a demo client app generated with [yo angular generator](https://github.com/yeoman/generator-angular) version 0.11.1. This is not part of the docker-compose file because this project relates to the API. The client (when finished) is provided as a reference implementation. Information about how to build and develop it will be included in the client README (TBC).

## Deployment

Because the app is built with Docker containers it will deploy reliably and repeatably anywhere that has working Docker and docker-compose installations.
