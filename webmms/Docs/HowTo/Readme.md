# WebMM &ndash; Web-based Message Manager

This project serves as a web-server interface for the RRS Message Manager system.

<!-- The intended sequence diagram is: -->

<!-- ![Browser &lArr;TCP&rArr; Web Server &lArr;UDP/TCP/MQTT&rArr; Message Manager Server](Docs/Diagrams/PowerPoint_Diagrams/Sequence_Diagram.svg) -->

## Requirements

- The Browser is Chrome
- Python3.6 or newer
- IP and Port of the Broker (Mosquitto)
- Packages:
	- Flask         						: 1.0.2
	- paho-mqtt                             : 1.4.0
	- configparser                          : 3.5.0
	- lxml                                  : 4.3.0

## Usage Instructions

- Windows:
-   - Install Python3.6
-   - Run a virtual environment: https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/
-   - Install above packages with pip install "package name"
-   - Run your local broker or use the one on the project mosquitto.exe file on "\webmm\Source\BackEnd\mos1.14" directory
-   - use the GPS node for testing, run Windows_Start_GPS_Interface.bat file on
    "\webmm\Source\BackEnd\GPS Test\External_Interfaces\GPS\Source" directory
-   - Open a command prompt and navigate to direcory "\webmm\Source\BackEnd"
-   - Set The flask app to server "set FLASK_APP=server.py"
-   - Run flask app "flask run" or specify the port "flask run --host=0.0.0.0 --port=5000"
-   - Server will start running, open browser and run it on localhost "http://localhost:5000/" or given url if you didn't
    specify host as 0.0.0.0
-   - Click the Pipes button and then click add new pipe 
- 	- Enter IP, Port of broker, the pipe name, then select the XML you want to use (also enter the system name and destination)     and then press connect
-   - Select which message you want to send and then wait for the response

- Linux:
-   - Install python3.6: https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f
-   - Run a virtual environment: https://www.caseylabs.com/how-to-create-a-python-3-6-virtual-environment-on-ubuntu-16-04/
-   - Install above packages with pip3.6 install "package name"
-   - Run your local broker
-   - Open a command prompt and navigate to direcory "\webmm\Source\BackEnd"
-   - export The flask app to server "export FLASK_APP=server.py"
-   - Run flask app "flask run" or specify the port "flask run --host=0.0.0.0 --port=5000"
-   - Server will start running, open browser and run it on localhost "http://0.0.0.0:5000/" or given url if you didn't specify host as 0.0.0.0.
-   - Click the Pipes button and then click add new pipe 
- 	- Enter IP, Port of broker, the pipe name, then select the XML you want to use (also enter the system name and destination)     and then press connect
-   - Select which message you want to send and then wait for the response

- RaspberryPi:
-   - If there is trouble installing Python 3.6 run:
	-	1. https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f 
	-	2. sudo apt-get install software-properties-common
-   - If there is trouble installing lxml run: 
	-	1. sudo apt-get install libxml2-dev libxslt-dev python3-dev 
	-	2. use easy_install lxml instead of pip3.6 install lxml.
-   - run your local broker
-   - Open a command prompt and navigate to direcory "\webmm\Source\BackEnd"
-   - export The flask app to server "export FLASK_APP=server.py"
-   - Run flask app "flask run" or specify the port "flask run --host=0.0.0.0 --port=5000"
-   - Server will start running, open browser and run it on localhost "0.0.0.0:5000/" or given url if you didn't specify host as 0.0.0.0.
-   - Click the Pipes button and then click add new pipe 
- 	- Enter IP, Port of broker, the pipe name, then select the XML you want to use (also enter the system name and destination)     and then press connect
-   - Select which message you want to send and then wait for the response

# Dockerize Webmms

-- This script will help you install docker, dockerize webmms, load webmms to a container and executing the webmms from docker
> **Note:** To make the install script executable, call `chmod +x script_name.sh`

# Docker installation
-- Run the included install script:
`./install_docker_ubuntu_18.04.sh`

# Downloading Meesage manager
  *	Clone message manager from git:
	- http://rrsbitbucket.rrs.co.za:7990/scm/gpet/webmm.git
  * Navigate to “BackEnd Directory”
	- webmm/Source/BackEnd/


# Dockerize/Build WebMMS image
-- Run this script to create webmms image:
`./dockerize_webmms_ubuntu_18.04.sh`

# run webmms image you created above
  * you will need:
    -  full path to your SICD directory
	-  full path to a script called 'recordedMessages.json' with empty curly brackets {}
  
  * Edit the 'run_webmms_ubuntu_18.04.sh' script
    -  replace /full/path/to/SICD with your SICD full path and
	-  replace /full/apth/to/recordedMessages.json with your full path to recordedMessages.json script
  * Run the script:
      `./run_webmms_ubuntu_18.04.sh`

## run these scripts if you wwant to deploy your image to another system
# Saving WebMMS image
-- Run the script:
`./save_webmms_image_ubuntu_18.04.sh`

# Loading WebMMS tar file to your docker
-- Run the script:
`./load_webmms_ubuntu_18.04.sh`