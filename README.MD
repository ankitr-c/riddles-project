# STEP 1:
    
    change directory to Backend folder

# STEP 2:
    
    open main.py file in any editor.

    replace this part ""Private-IP-of-your-VPC-Mongo-Database-VM"" with the private ip of your database vm.

# STEP 3:
    
    change directory to Execution-Script Folder.

# STEP 4:
    imp changes in DockerScript.sh file:
   
    <staticip-multivm-dockerproject>_backend
   
    change the name between angle brackets, insert your project name

    in my case it will be:

        vpc-project_backend

# STEP 5:

    change permissions and execute the docker script.
    
    commands:

        1. chmod +x DockerScript.sh
        2. ./DockerScript.sh


    