# Environment

There are virtual computers available. The IP addresses (available from a
private network in laboratory only) are: **10.100.0.41-53**.

The credentials are as usual:

- username: **student**
- password: **student**
- root access via **sudo**

# Agenda

Add remaining services to the containerize environment and try to expose the call function
via custom-built REST API.

## Git repository

Update your git repository with a new branch.

In this branch, implement changes and when done with testing, merge it with main.

## Set up connection to AMI

Follow these steps in order to make Asterisk AMI accessible via custom-built REST API.
Use it to originate a call from local extensions.

1. Create a docker container for Python project and Nginx.
1. Configure Nginx to use SSL certificates and to pass given requests to upstream backend.
1. Create a simple REST API using FastAPI library and connect it to Asterisk AMI using
the code we created in the previous lecture.


Finish the topology by setting up Kamailio container as well.



## Useful commands

```bash
# generate a selfsigned certificate and key for nginx
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout nginx-selfsigned.key -out nginx-selfsigned.crt
# generate dhparams for nginx
openssl dhparam -out dhparam.pem 4096
# create a new poetry project
poetry new voip2_backend
# install a new dependency in python project
poetry add fastapi
# build python project
poetry build
```
