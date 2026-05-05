# Environment

There are virtual computers available. The IP addresses (available from a
private network in laboratory only) are: **10.100.0.41-53**.

The credentials are as usual:

- username: **student**
- password: **student**
- root access via **sudo**

# Agenda

Communicate and direct Asterisk via AMI interface to establish a call.

## Git repository

Update your git repository with a new branch.

In this branch, implement changes and when done with testing, merge it with main.

## Set up connection to AMI

Follow these steps in order to make Asterisk AMI listen on given port.
Use it to originate a call from local extensions.

1. Add manager.conf file to your Asterisk configuration.
1. Modify docker compose configuration to allow incoming connections to AMI port.
1. Use telnet to test the connection and then implement a simple script to make a call.
