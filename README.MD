# STEP 1:

    change directory to Execution-Script

        command: cd Execution-Script

# STEP 2:
    
    open default config file in any editor and make the following changes.

        command: nano default

        replace this part ""your-backend-vm-private-ip"" with the private ip of your "Backend-VPC-VM"

        save and exit.
             
# STEP 3:
    Imp changes in DockerScript.sh file

        change the name of the project to your project: <staticip-multivm-dockerproject>_frontend

        In my case: vpc-project_frontend
    

# STEP 4:

    change permission and execute the docker script.
    
    commands:  
        1. chmod +x DockerScript.sh
        2. ./DockerScript.sh


        