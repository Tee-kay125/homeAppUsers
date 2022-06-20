#!/bin/bash
sudo docker save webmms:latest | gzip > docker_files/webmms.tar.gz