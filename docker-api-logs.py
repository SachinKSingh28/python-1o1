#!/usr/bin/python

import docker;

client = docker.from_env()

client.containers.run("ubuntu", detach=True)

container = client.containers.get('ldap')
container.logs()
container.stop()
