#!/bin/bash

# Check if port/argument is passed and exit if it is not
if [ $# -eq 0 ]
  then
    echo "Please provide a port number"
    exit 1
fi

# read the argument
webmms_port_number=$1

#get current working directory
cwd=$(pwd)

# get full path of the directory, and append SICD,
# use the full path to check if SICD exist, if it doesn't, create it
full_path_to_SICD="$cwd/SICD"
if [ ! -d "$full_path_to_SICD" ]; then
  mkdir SICD
fi

# get full path of the directory, and append pipes_config,
# use the full path to check if pipes_config exist, if it doesn't, create it
full_path_to_pipes_config="$cwd/pipes_config"
if [ ! -d "$full_path_to_pipes_config" ]; then
  mkdir pipes_config
fi

# get full path of the directory, and append scriptingFiles,
# use the full path to check if scriptingFiles exist, if it doesn't, create it
full_path_to_scriptingFiles="$cwd/scriptingFiles"
if [ ! -d "$full_path_to_scriptingFiles" ]; then
  mkdir scriptingFiles
fi

# create run_webmms_ubuntu_18.04.sh
echo "docker run --volume $full_path_to_SICD:/app/SICD --volume $full_path_to_pipes_config:/app/pipes_config --volume $full_path_to_scriptingFiles:/app/scriptingFiles -p $webmms_port_number:80 webmms" > run_webmms_centos_8.sh

# Load webmms image to local docker
docker load < webmms.tar.gz

# make sh script executable

chmod +x ./run_webmms_centos_8.sh
chmod +x ./stop_docker_image.sh

echo "installation complete, copy your xml files to generated SICD directory and run './run_webmms_centos_8.sh' to start WebMM"