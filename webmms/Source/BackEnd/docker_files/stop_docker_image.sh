#!/bin/bash
sudo docker stop $(sudo docker ps -q --filter ancestor=webmms)