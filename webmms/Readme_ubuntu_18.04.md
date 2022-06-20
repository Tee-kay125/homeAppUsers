# WebMM

**WebMM version: V0.1.0**

# Requirements
* Chrome browser (latest version is preferred)
* Ubuntu 18.04 (the approved MWS OS)
* Docker (can run `./install_docker_ubuntu_18.04.sh`. Only needs to be run if docker is not installed yet)

Note: Do not run any of these commands with sudo to prevent file permissions

# First time install and setup

* Run `./create_webmms_volume_and_set_port.sh PORT_NUMBER` where `PORT_NUMBER` is your preferred WebMM host port. One only needs to run this script again if the port number needs to be changed.

# After first time install and setup

After the initial setup and instal (which only needs to happen once) the following usage instructions applies:

### To run WebMM 
* Type -> `./run_webmms_ubuntu_18.04.sh`
    
### To stop WebMM
* Run `./stop_docker_image.sh`

### General usage instructions

* After WebMM starts, open your browser and enter your WebMM IP and the Port number you provided when running the script. Example `http://127.0.0.1:5007`. Note! The IP `127.0.0.1` will probably not work when the WebMM is deployed from a docker image. Also make sure the firewall is set up correctly or disabled when using the dockerised WebMM.
* At the bottom left menu bar click the `Pipes` button.
* At top left, click `Add new pipe`.
* Enter the MQTT broker IP and port, the pipe name, and then select the XML you want to use. Also enter the system name and destination and then press `Connect`.
* After the pipe is created messages will be displayed in a tree structure on the left most panel.
* Collapse and expand to display messages.

### User Guide
* refer to adcs_user_guide.pdf or adcs_user_guide.pptx

### Exclusions

Given that the WebMM is still under development and that this is an early release the following functionality will not work:
* Command response and request response messages cannot be published.
* Messages will not validated.
* Messages cannot be recorded. We define recorded here as specific messages selected by the user.
* Selected messages cannot be saved as favourites list.
* The automatic logging of messages. This feature is different to message recording in that all messages received are stored. One does not select which ones are stored.
* The ability to open messages on new tabs.
* Do not select messages in the message tree too quickly. Wait at least 1 second before clicking a message.

These limitations will however be addressed in future releases.

# Development

Note: For more detailed development information see `Docs/HowTo/Readme.md`. For normal everyday usage of the WebMM reading this document is not required.