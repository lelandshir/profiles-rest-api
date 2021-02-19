# Python_Django Rest API Application

### Technologies

- Python | Django 2.2 | Django REST Framework 3.9 | Vagrant | VirtualBox | ModHeaders
- Deploy dev server to AWS

### Development Server

#### Vagrant

1. Allows us to describe the type of server needed for an app
1. Save the configuration as a Vagrant file for ease of reproducing and sharing w/ other devs
1. Vagrant uses Virtualbox (a Hypervisor) (by Oracle) to create a Virtual Server as we described; our code and requiremwnts will run here,
   isolated from our local machine - We can run the same software as a true production server here as well!
1. We can wasily create and destroy the server as we see fit

### Application Code

#### Python, Django, & Django REST Framework

1. Python, a coding language, is the 1st layer and serves logic for the app
1. Django, a web framework for Python, is the 2nd layer. It standardizes apps and has a pre-defined set of code to perform common actions
1. Django REST Framework, provides a set of features for making standard REST APIs

### Tools

#### IDE, Git, ModHeaders

- ModHeaders is a Chrome Extension for easily modifying HTTP Headers when testing an API

### Set Up Dependencies

1. Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads) (OS X hosts)
1. Install [Vagrant](https://www.vagrantup.com/downloads) (MAC OS X); Check In terminal with `vagrant --version` to See something like `Vagrant 2.2.14`
1. Install [ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en)
1. `git init, touch readme, .gitignore`. Here's a standard `.gitignore` for a python vagrant project: [gitignore](https://gist.github.com/LondonAppDev/dd166e24f69db4404102161df02a63ff)
1. Create License File: [License File](https://choosealicense.com/licenses/mit/) - to make it clear to others what they can do with this code if they were to reuse it, and to protect yourself from a lawsuit.
1. `git add .`, `git commit -am'first commit'`

#### SSH Key

1. ➜ `ls ~/.ssh` Generate an SSH Key: `ssh-keygen -t rsa 4096 -C "lelandshir@gmail.com"`: this runs the SSH Key Generation Tool. The command says "Create a new key that is an RSA type, is 4,096 bytes, with a comment so that you can ID what the key is for if you need to. Press enter to generate the key/pair, and enter again to save it in it's default path (recommended). Create a passphrase for the key as an extra layer of security against web crawlers. They can't use the key w/o a passphrase if they do steal it.
1. `cat ~/.ssh/id_rsa.pub` to grab key and head to gitHub to add it.
1. Create a new repo on github, and `git remote add origin <url>` to configure path, then `git branch -M main` to configure a `main` branch, then `git push -u origin main`

### Create A Vagrant File

- `vagrant init ubuntu/bionic64` : init project w/ new vagrant file and bases it on ubuntu/bionic64 base image, [Vagrantfile](https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682)

1. Run `vagrant up` to download base image specified in Vagrantfile, then uses VB to create a new VM and run the provisioning script when it starts the VM. We can then use our dev server and connect to it.
1. Once the VM is created, connect to it: `vagrant ssh` command using ssh, disconnect from the machine by typing `exit`
1. The dev server is a VM, by default the file system is not sync'd. Files on DS are diff from files on local machine. Vagrant creates a sync'd directory on our the Vagrant server that updates itself every time we make changes.

### Create Python Virtual Environment

1. In Vagrant server, cd into `/vagrant` directory
1. Create a PVE with Python 3 by running `python -m venv ~/env` --This path is in the home directory of the Vagrant Server (as opposed to the Vagrant folder which is sync'd to our local machine). We create the Python Virtual Environment and its dependencies here because we do not want it to sync with our local machines.

#### Activating and deactivating the Virtual Environment with Python

1. VE's need to be actived and deactivated
1. When activated, all dependencies run through the Python application will be pulled from the Virtual Environment instead of the base OS.
1. activate by running `source ~/env/bin/activate` - this is the path to the activate script within the environment
1. You'll know you're in the virtual environment because the name of the VE you're working on will prefix itself to the CL input.
1. deactivate by running `deactivate`

### Install required Python Packages

1. `touch requirements.txt`
1. This is where to list all the packages needed and the specfic versions to use. It's good practice to pin dependencies w/ a version, otherwise the latest version will be installed. There could be an update that breaks your project! [Versions: Python Packages](https://pypi.org/)
1. After adding the requirements, connect to the vagrant server and be sure the virtual environment is activated. Install the requirements by running: `pip install -r requirements.txt `

# Profiles REST API
