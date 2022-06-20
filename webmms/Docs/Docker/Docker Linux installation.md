# Uninstall old version
*  sudo apt-get remove docker docker-engine docker.io containerd runc

# SET UP THE REPOSITORY
1. Update the apt package index:
    * sudo apt-get update
2. Install packages to allow apt to use a repository over HTTPS:
    * sudo apt-get install \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg-agent \
      software-properties-common
3. Add Docker’s official GPG key:
    * curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   
    # Verify that you now have the key with the fingerprint
      * sudo apt-key fingerprint 0EBFCD88
    # output for the above code
      * pub   rsa4096 2017-02-22 [SCEA]
        9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
        uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
        sub   rsa4096 2017-02-22 [S]
4. Use the following command to set up the stable repository (To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the            commands below)
    * sudo add-apt-repository \
      "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) \
      stable"

# INSTALL DOCKER ENGINE - COMMUNITY
1. Update the apt package index.
    * sudo apt-get update
2. Install the latest version of Docker Engine
    * sudo apt-get install docker-ce docker-ce-cli containerd.io
3. Verify that Docker Engine - Community is installed correctly by running the hello-world image.
    * sudo docker run hello-world

# Configure Docker to start on boot.
* sudo systemctl enable docker
# To disable this behavior, use disable instead.
* sudo systemctl disable docker

# Uninstall Docker Engine - Community
1. Uninstall the Docker Engine - Community package:
    * sudo apt-get purge docker-ce
2. Images, containers, volumes, or customized configuration files on your host are not automatically removed. To delete all images, containers, and volumes:
    * sudo rm -rf /var/lib/docker

# Other settings
1. Reload the systemctl configuration.
    * sudo systemctl daemon-reload
2. Restart Docker.
    * sudo systemctl restart docker.service