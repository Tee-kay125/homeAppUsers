WebMM Installation Process for CentOS8
======================================
This HowTo requires an internet connection. This Docker image has been verified to work
in RO OS mode as well.


1) Clone WebMM repo from BitBucket:
   # git clone http://rrsbitbucket.rrs.co.za:7990/scm/gpet/webmm.git


2) Install Docker:
   Navigate to "Source/BackEnd/docker_files" and run the following script:
   # sh ./install_docker_centos8.sh


3) Start the Docker service (if it is not started already):
   # systemctl status docker  (check if the service is running)
   # systemctl start docker   (start the docker service)


4) Run WebMM Image:
   This step contains 2 options, the first being to create and backup the WebMM image from the repo
   or load up a backed up image into Docker already. Always do 3.2 and only do 3.1 if
   no backup Docker image is available.

   4.1) Create WebMM Docker image (This step requires internet):
        4.1.1) Open a terminal in "Source/BackEnd" and run the following command:
               # docker build --tag=webmms .

        4.1.2) Again in "Source/BackEnd", create a backup of the Docker image:
               # docker save webmms:latest | gzip > docker_files/webmms.tar.gz
               Note: This will create the backup in "docker_files/webmms.tar"

   4.2) Restore a backed up Docker image:
        4.2.1) Copy the backed up Docker image and the following scripts from "Source/BackEnd/docker_files" 
               to the directory you plan to deploy WebMM to:
               - create_webmms_volume_and_set_port_centos8.sh
               - install_docker_centos8.sh
               - stop_docker_image.sh
               - webmms.tar.gz (backup Docker image has to have this name for scripts to work)

        4.2.2) In the WebMM deployment directory, load the backed up Docker image using the following script:
               # sh ./create_webmms_volume_and_set_port_centos8.sh {WebMM port}
               e.g. # sh ./create_webmms_volume_and_set_port_centos8.sh 5005

               Note: This step will autogen a run script called "run_webmms_centos_8.sh".


5) Copy the relavent XML and MIC to the WebMM deployment directory "SICD" directory.

6) Start the WebMM Docker image by running the the following script in the WebMM
   deployment directory:
   # sh ./run_webmms_centos_8.sh &

   Note: Make sure Docker is running (Step 3).


7) Stop WebMM by running the following script in the deployment directory:
   # sh ./stop_docker_image.sh


