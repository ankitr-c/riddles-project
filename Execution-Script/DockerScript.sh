#!/bin/bash

# Author: Ankit Raut 

# Description: This Docker Script will install and configure the nginx for frontend and also start the containers for front end.

setVariables()
{
    #defining directory path.
    path="/home/ankitraut0987/vpc-project"
    
    #defining nginx path
    nginx_path="/etc/nginx/sites-enabled"

}

getVariables()
{
    echo "Path:$path"
    echo "Nginx Path:$nginx_path"

}


setVariables

#Install Nginx Server
# sudo apt-get install nginx -y >/dev/null || { echo "Failed to Install Nginx Server"; exit 1; }
sudo apt-get install nginx -y || { echo "Failed to Install Nginx Server"; exit 1; }


#Configuring Nginx Server:
sudo rm "$nginx_path/default" || echo "Default Config File Not Found"
cd "$path/Execution-Script/"
sudo cp "default" "$nginx_path/"
sudo systemctl restart nginx

echo "*** Successfully Configured Nginx ***"

cd

# sudo apt-get install docker -y >/dev/null && echo "** Successfully Installed Docker **" || { echo "Failed to Install Docker"; exit 1; }
# sudo apt-get install docker-compose -y >/dev/null && echo "** Successfully Installed Docker-Compose **" || { echo "Failed to Install Docker-Copmose"; exit 1; }

# Installing Docker.
sudo apt-get install docker -y && echo "** Successfully Installed Docker **" || { echo "Failed to Install Docker"; exit 1; }

# Installing Docker-Compose.
sudo apt-get install docker-compose -y && echo "** Successfully Installed Docker-Compose **" || { echo "Failed to Install Docker-Copmose"; exit 1; }



cd "$path"

sudo docker-compose down && echo "Docker Is Down Now" || echo "Docker Already Down"

# sudo docker rmi staticip-multivm-dockerproject_frontend || echo "Error deleting frontend image"
sudo docker rmi vpc-project_frontend || echo "Error deleting frontend image"

sudo docker-compose up -d || echo "error in compose file"


