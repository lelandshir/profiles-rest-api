# Python_Django Rest API Application Code

### Technologies

- Python | Django 2.2 | Django REST Framework 3.9 | Vagrant | VirtualBox | ModHeaders
- Deploy dev server to AWS

### 1. Development Server Notes:

#### Vagrant

1. Allows us to describe the type of server needed for an app
1. Save the configuration as a Vagrant file for ease of reproducing and sharing w/ other devs
1. Vagrant uses Virtualbox (a Hypervisor) (by Oracle) to create a Virtual Server as we described; our code and requiremwnts will run here,
   isolated from our local machine - We can run the same software as a true production server here as well!
1. We can wasily create and destroy the server as we see fit

#### Python, Django, & Django REST Framework

1. Python, a coding language, is the 1st layer and serves logic for the app
1. Django, a web framework for Python, is the 2nd layer. It standardizes apps and has a pre-defined set of code to perform common actions
1. Django REST Framework, provides a set of features for making standard REST APIs

`Tools:` IDE, Git, & ModHeaders: a Chrome Extension for easily modifying HTTP Headers when testing an API

### 2. Set Up Development Environment

#### Installations

1. Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads) (OS X hosts)
1. Install [Vagrant](https://www.vagrantup.com/downloads) (MAC OS X); Check In terminal with `vagrant --version` to See something like `Vagrant 2.2.14`
1. Install [ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=en)

#### Create Git Project

1. `mkdir profiles-rest-api`, `git init`, `touch README.md`, `.gitignore`. Here's a standard gitignore file for a python/vagrant project: [gitignore](https://gist.github.com/LondonAppDev/dd166e24f69db4404102161df02a63ff)
1. Create License File: [License File](https://choosealicense.com/licenses/mit/) - to make it clear to others what they can do with this code if they were to reuse it, and to protect yourself from a lawsuit.
1. `git add .`, `git commit -am'first commit'`

#### Generate SSH Key for this Project

1. ➜ `ls ~/.ssh` Generate an SSH Key: `ssh-keygen -t rsa 4096 -C "lelandshir@gmail.com"`: this runs the SSH Key Generation Tool. The command says "Create a new key that is an RSA type, is 4,096 bytes, with a comment so that you can ID what the key is for if you need to. Press enter to generate the key/pair, and enter again to save it in it's default path (recommended). Create a passphrase for the key as an extra layer of security against web crawlers. They can't use the key w/o a passphrase if they do steal it.
1. `cat ~/.ssh/id_rsa.pub` to grab key and head to gitHub to add it.
1. Create a new repo on github, and `git remote add origin <url>` to configure path, then `git branch -M main` to configure a `main` branch, then `git push -u origin main`

### 3. Creating Development Server

#### Create A Vagrant File

- In thr root of the project, run `vagrant init ubuntu/bionic64` to initialize the project w/ a new `Vagrantfile` and base it on the ubuntu/bionic64 base image. [Vagrantfile](https://gist.github.com/LondonAppDev/199eef145a21587ea866b69d40d28682)

#### Configure Vagrant Box

1. Run `vagrant up` to download base image specified in Vagrantfile, then uses VB to create a new VM and run the provisioning script when it starts the VM. We can then use our dev server and connect to it.

#### Running and Connecting to Dev Server

1. Once the VM is created, connect to it: `vagrant ssh` command using ssh, disconnect from the machine by typing `exit`
1. The dev server is a Virtual Machine, by default the file system is not sync'd. Files on the Dev Server are different from the files on the local machine. Vagrant creates a sync'd directory on our the Vagrant server that updates itself every time changes are made to files.

### 4. Creating A Django App

#### Create Python Virtual Environment

1. In Vagrant server, cd into `/vagrant` directory
1. Create a PVE with Python 3 by running `python -m venv ~/env` --This path is in the home directory of the Vagrant Server (as opposed to the Vagrant folder which is sync'd to our local machine). We create the Python Virtual Environment and its dependencies here because we do not want it to sync with our local machines.

#### Activating and deactivating the Virtual Environment with Python

1. VE's need to be actived and deactivated
1. When activated, all dependencies run through the Python application will be pulled from the Virtual Environment instead of the base OS.
1. activate by running `source ~/env/bin/activate` - this is the path to the activate script within the environment
1. You'll know you're in the virtual environment because the name of the VE you're working on will prefix itself to the CL input.
1. deactivate by running `deactivate`

#### Install required Python Packages

1. `touch requirements.txt`
1. This is where to list all the packages needed and the specfic versions to use. It's good practice to pin dependencies w/ a version, otherwise the latest version will be installed. There could be an update that breaks your project! [Versions: Python Packages](https://pypi.org/)
1. After adding the requirements, connect to the vagrant server and be sure the virtual environment is activated. Install the requirements by running: `pip install -r requirements.txt `

#### Create a new Django Project & App

1. In terminal make sure you're connected to the Vagrant server and in the `/vagrant/` directory, and working on the Virtual Environment created.
1. Run `django-admin.py startproject profiles_project .` - This calls the django-admin script and passes in the startproject argument and specifies the name of the project, then the location - not specifying the location using the `.` creates a sub folder, so use the `.` to place it in the root
1. the project directory will be created alongside the manage.py script
1. Now that the Django project has been created, create an app within the project - A Django Project can consist of one or more sub-applications within the project that we can use to separate functionality within the project
1. `python manage.py startapp profiles_api` - This creates a new django app (sub folder) in the directory

#### Enable App in Django Settings File

1. Open `profiles_project/settings.py` - look for the `INSTALLED_APPS` block
- This is where you list apps used for the project. You can install via an external dependency or create a new app and add it to the list
1. Add:
- `'rest_framework',` - the app within the django rest framework installed earlier
- `'rest_framework.authtoken'` - allows for use of auth token functionality out the box with rest framework
- `'profiles_api',` - the app created

#### Test and commit changes 
1. Be connected to Vagrant and to the virtual environment, and run `python manage.py runserver 0.0.0.0:8000` - this tells django to run the python dev server, make it available on all network adapters available on the dev server, start it in port 8000 where it can be accessed. Remember that the Vagrantfile specifies port 8000 as well
1. Don't worry about migration warning yet, head to `127.0.0.1:8000` in the broswer to see a "success" screen
1. ctrl + C to stop the server
1. Commit Changes


### 5. Django Models
1. Models describe the data we need for the app, Django uses these models to set up and configure the db to store data properly
1. Each model maps to a table in the DB, Django handles the relationships between models and the db so that we don't have to use SL to interact with the DB directly

#### User Profile Model
1. Out of the box, Django comes with a default user model used for the standard auth system and Django Admin. We'll override this model with a custom model that allows for use of an email address instead of the standard username that comes with the Django default model
1. Best Practice: Keep all DB models in `models.py` within the app
1. In `models.py`:
- `from django.contrib.auth.models import AbstractBaseUser`
- `from django.contrib.models import PermissionMixin`
- Based on the docs, these are the standard base classes needed to override or customize the default user Django model
```
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    # the python standard for writing a doc string to explain what the class is and does
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # Fields for permission system
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Specify model mgmt, Django needs a custom model mgr so it knows how to create users using the CLI tool
    objects = UserProfileManager() 
    # override name fields and requirements
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    # functions for django to get data
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return a str representation of user"""
        return self.email
```






## Profiles REST API
