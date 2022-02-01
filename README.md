Blog on how to prevent BYOL Autonomous Database creation in OCI using Function with Event


Oracle Cloud Infrastructure Events and Function enables you to create automation based on the state changes of resources throughout your tenancy. Use Events to allow your development teams to automatically respond when a resource changes its state.
Here are some examples of how you might use Events and Function: 
    •	Setup Function to change ADB license to “License Included”, whenever BYOL is used to create or alter ADB. 
SETUP, CREATE & DEPLOY OCI FUNCTION
Follow one of the methods mentioned in Startup guides to create a function and deploy on OCI
https://www.oracle.com/webfolder/technetwork/tutorials/infographics/oci_faas_gettingstarted_quickview/functions_quickview_top/functions_quickview/index.html
For the purpose of the blog, we will use an OCI Compute Instance as a staging area to create the functions:
https://www.oracle.com/webfolder/technetwork/tutorials/infographics/oci_functions_vm_quickview/functions_quickview_top/functions_quickview/index.html
Please follow the blog and complete the steps as directed.
The Major Sections to achieve the same are as below:
	Setting up your Tenancy
	Complete Tenancy Set-up
	Set up Local Dev Environment
	Set up Fn Project CLI in Local Dev Environment
	Create, Deploy and invoke your Function

SECTION 3 (SETUP YOUR DEV ENVIRONMENT) assumes that you have Docker installed already.
You could refer below for example on how to install Docker on OCI Compute:  




Docker Installation Example:
Login as opc user to the Compute Instance.
sudo yum install docker -y
sudo yum install docker-engine -y
sudo systemctl start docker
sudo systemctl enable docker
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

[opc@func-inst-blk ~]$ sudo docker version
Client: Docker Engine - Community
 Version:           19.03.11-ol
 API version:       1.40
 Go version:        go1.15.2
 Git commit:        1f5403e
 Built:             Mon Oct 19 12:48:26 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          19.03.11-ol
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.15.2
  Git commit:       1f5403e
  Built:            Mon Oct 19 12:46:43 2020
  OS/Arch:          linux/amd64
  Experimental:     false
  Default Registry: docker.io
 containerd:
  Version:          v1.2.0-rc.0-108-gc444666
  GitCommit:        c44******c7c39
 runc:
  Version:          spec: 1.0.1-dev
  GitCommit:
 docker-init:
  Version:          0.18.0
  GitCommit:        fdasf
[opc@func-inst-blk ~]$

[opc@func-inst-blk ~]$ sudo docker login iad.ocir.io
Username: or02/oracleidentitycloudservice/emailid@oracle.com
Password:
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[opc@func-inst-blk ~]$

iad.ocir.io -- Replace the region with your base region where the functions are created

SECTION 4 (SET UP FN PROJECT CLI) requires you to setup and complete Function CLI, check below for an example:


curl -LSs https://raw.githubusercontent.com/fnproject/cli/master/install | sh
fn create context oci_function_ctx --provider oracle-ip
fn use context oci_func_ctx
fn update context oracle.compartment-id ocid1.compartment.oc1..XXXXXXXXXXXXXXXXXXa
fn update context api-url https://functions.us-ashburn-1.oraclecloud.com
fn update context registry iad.ocir.io/tenancyname/reponame
oci_function_ctx – Function Context Name
ocid1.compartment.oc1..XXXXXXXa – Compartment OCID where function is placed
https://functions.us-ashburn-1.oraclecloud.com  – Replace region based on the region where the function is being created
SECTION 5 (CREATE, DEPLOY AND INVOKE THE FUNCTION) requires you to create an application, use below command line to create the app for your custom application:

fn create app fn_byol_adb --annotation oracle.com/oci/subnetIds='["ocid1.subnet.oc1.iad.aaxxxxxxxa"]'
fn list apps
In the above example,
 “fn_byol_adb” is the application name
“subnetIds='["ocid1.subnet.oc1.iad.aaxxxxxxxa"]'” – Provide the Subnet OCID where the application will be placed 




After Application creation, a function needs to be created under the app. Refer to the below example:
Download code repo from github
git clone https://github.com/gomsey3004/fn_byol_adb.git

cd fn_byol_adb
--Change Directory to the created app
fn -v deploy --app fn_byol_adb

You can invoke the function simply from command line, using an example as below:

Once the Function is deployed, you can check the details of the function from the console:







•	Event Creation to invoke function to change BYOL to license included.
 
 
  



 

 
