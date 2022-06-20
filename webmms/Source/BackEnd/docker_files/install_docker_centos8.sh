#!/bin/bash
dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
yum remove podman -y
yum install docker-ce --nobest --allowerasing -y
systemctl start docker