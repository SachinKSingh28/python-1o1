#!/usr/bin/python

import docker;

client = docker.from_env()

client.containers.run("ubuntu", detach=True)
