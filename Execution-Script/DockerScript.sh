#!/bin/bash

# Author: Ankit Raut 

# Description: This Docker Script will install docker, dockercomopose and configure the Backend.

setVariables()
{
    #defining directory path.
    path="/home/ankitraut0987/vpc-project"

}

getVariables()
{
    echo "Path:$path"

}


setVariables

cd

# sudo apt-get install docker -y >/dev/null && echo "** Successfully Installed Docker **" || { echo "Failed to Install Docker"; exit 1; }
# sudo apt-get install docker-compose -y >/dev/null && echo "** Successfully Installed Docker-Compose **" || { echo "Failed to Install Docker-Copmose"; exit 1; }


sudo apt-get install docker -y && echo "** Successfully Installed Docker **" || { echo "Failed to Install Docker"; exit 1; }
sudo apt-get install docker-compose -y && echo "** Successfully Installed Docker-Compose **" || { echo "Failed to Install Docker-Copmose"; exit 1; }

cd "$path"

sudo docker-compose down && echo "Docker Is Down Now" || echo "Docker Already Down"

# sudo docker rmi staticip-multivm-dockerproject_backend || echo "Error deleting backend image"
sudo docker rmi vpc-project_backend || echo "Error deleting backend image"



sudo docker-compose up -d || echo "error in compose file"

