Correspondence
==============================

A web service to produce business correspondence.


LICENSE: BSD

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* Docker
* fig

Open a terminal at the project root and type::

    $ sudo fig build

You can now run the ``fig up`` command::

    $ sudo fig up

This will build your database, api and webserver, and link them to each other.


Deployment
------------

Because the app is built with Docker containers it will deploy reliably and repeatably anywhere that has a working Docker and fig installations.
