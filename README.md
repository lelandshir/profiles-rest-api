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
1. Setup Python for VS Code (MacOS 2020)
- download latest version of python [python](https://www.python.org/downloads/)
- In VS Code go to extensions and search for `python` and install the extension w/ the most installations 
- Get execuable path for python: Open a new Terminal, run `python3` and `import sys` (system module which can print the executable path by typing, `print(sys.executable)`, copy that path
- In VS Code go to `Code, Preferences, Settings`: open the `settings.json` by clicking the file icon in the top right corner of the VSC (`.vscode/settings.json`)
- add the bottom of the file add `"python.pythonPath": "/Library/Frameworks/Python.framework/Versions/3.9/bin/python3"` and save the file
- Install the Python Linter when prompted by VS Code and run a python script to test

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
1. Out of the box, Django comes with a default user model used for the standard authentication system and Django Admin. We can override this model with a custom model that allows for use of an email address instead of the standard username that comes with the Django default model.
1. Best Practice: Keep all DB models in `models.py` within the app directory
1. In `models.py`:
- `from django.contrib.auth.models import AbstractBaseUser`
- `from django.contrib.auth.models import PermissionsMixin`
- Based on the docs, these are the standard base classes needed to override or customize the default user Django model... Next, the UserProfile Model:
```
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    # the abive is the python standard for writing a doc string to explain what the class is/does
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

#### Explaining The Code:
1. Created a UserProfile class and passed in the `AbstractBaseUser` and `PermissionsMixin` which allow customization of the default Django User Model as needed; then defined the required fields for the model. Note that `email` and `name` will become columns on the UserProfile Database Table.
1. Added fields for the permissions system; `is_active` (allows us to deactivate users if needed), and `is_staff` (to determine if user is a staff user which determines access level).
1. Specified a `USERNAME` field because we are overriding the `USERNAME` field by having users provide their email address and password when being authenticated rather than their username and password. The USERNAME field is required by default, we've simply switched it to be the email that is required instead. 
1. Specified additional `REQUIRED_FIELDS` list and added `name`. This says that at minimum the user must also give their name.
1. Added functions that are used for django to interact with the custom user model; "getters". 
- `Note`: When defining a function within a class we must pass `self` in as the first argument. This is the default python convention!
1. Specified string representation of the model; the item we want to return when we convert a UserProfile Obj into a string in python. 
- `Note`: `__str__(self)` is recommended for all django models, otherwise when you convert it to a string you won't return a meaningful output, so specify this function and return the field you want to use to identify this model.

#### Add A User Model Manager 
- `Required`: Django needs to have a custom model manager for the user model so it knows how to create and control users using the django command line tools
- The Django CLI provided command, `create-super-user`, makes it very easy to add super users to the system. A super user is an admin user with full control and accessibilty to the Django Admin and see all models in the DB
- Since the User Model was customized, you need to tell Django how to interact with the model to create instances of users where we no longer ask for a username (the default expectation), but instead an email (the change made in the class)
- The way managers work is you specify functions within the manager made to manipulate objects within the model that the manager is for 
- `Note`: PEP guidelines ask that two spaces separate classes [More Here](https://www.python.org/dev/peps/pep-0008/)

- In `models.py`:
2 spaces above the UserProfile class:
```
from django.contrib.auth.models import BaseUserManager

class UserProfileManager():
    """Manager for user profiles"""
    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Whoa there! You need an email address!')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
```

#### Explaining The Code:
1. Created UserProfileManager class
1. Imported `BaseUserManager` because we want to inherit from the default user manager in Django
1. Specified BaseUserManager as a parent class
1. Defined create_user function; for creating users with the Django CLI tool 
1. Provided a check to make sure an email value has been provided 
1. Normalized email address, makes second half of email address lower case - best practice
1. create user model - this creates a user model that the user manager is representing with `self.model` and sets the new object with the email and the name
1. Used the set_password function that comes w/ user model to encrypt the password and set it to a hash to protect against hackers/web crawlers (they can still reverse engineer if given enoug time, but this is best practice)
1. Saved the user, and passed in the DB to save the object to (described in Django docs)
1. Returned the user
1. Created super user and passed in self, ...x
1. We set `is_superuser = True` which is a BooleanObject auto provided by the permissions mixin

#### Set custom user model
- Configure Django Project to use the user model we created as the default user model as opposed to the one provided by Django
1. Set the User Model in `settings.py`. Scroll to the bottom and create a new line: 
- `AUTH_USER_MODEL = 'profiles_api.UserProfile'` - Set this to the app we want to retriebe the model from and the name of the model to use. Tells Django to look at this app and find this model and use it for auth in the project. Note: AUST_USER_MODEL is set to a string value.

#### Create Migrations and sync DB
- Create a migration file for the models added to the project. 
- Django manages the DB by creating a migration file that stores all steps required to make DB match Django models. 
- Each time we change models or add additional models you need to change the migration file; it will contain the steps required to modify the DB to match the updated models 
- `Example`: If you add a new model to the project, then you need to be able to create a new table in the DB. This is done via a migration
- You can create migrations with the Django Command Line Tool: 
1. cd to the root of the project directory and connect to vagrant dev server: `vagrant ssh`
1. cd into the `/vagrant` directory and activate virtual environment: `source ~/env/bin/activate`
1. Use the `manage.py` file to create migrations: `python manage.py makemigrations profiles_api`
1. This creates a new migration file in the project for the userProfile model; we shuold not have to modify these files
1. Now run the migration: `python manage.py migrate` - this runs all migrations in the project
1. Goes through Django Project and creates all required models/tables in the DB for any models and dependenices you have
- That is how you create and manage changes 

### 6. Setup Django Admin

- Enable the Django Adminon the project. A useful tool that lets you create an admin site for your project where you can inspect, manage and see your DB models

#### Create Superuser
1. You need to create a super user to do this, using the Command Line Tool, run: `python manage.py createsuperuser`
1. You'll be prompted for email, name, and password to create a superuser successfully

#### Enable the Django Admin on this Project
- By default the admin is enabled on all new projects, but newly created models must be registered with the admin so it knows you want to display that model in the admin interface
1. In `admin.py`:
```
from profiles_api import models

admin.site.register(models.)
```

#### Explaining the Code
1. import your models from your project 
1. Register models - this tells Django Admin to register UserProfile mdoel w/ admin site so it makes it accessible through the admin interface

#### Test The Django Admin
1. start the dev server: `python manage.py runserver 0.0.0:8000` (may need `--noreload`)
1. head to `http://127.0.0.1:8000/admin` and log in with the superuser credentials created 
1. Each section represents a different app in the project; 
- authtoken app is added from django rest framework when enabling tokens
- auth and autho is out-the-box with django and allows you to use the auth system
- then there's the app you created and the model registered
- Django looks at the camel cased singular class we defined and generates the name that way; it adds the `s` to the end becase it makes sense that there will be several created
- The model will show the super user created; the hashed password is shown and the last login along with fields available in the model
- commit!

- `Server Error Note`: I had a development environment issue in which the Vagrant server kept refreshing the files from my local machine when starting the python server: The `--noreload` flag sufficed!

### 7. Intro To API Views
- DRF offers helper classes used to help create API endpoints: APIView and Viewset

#### What is an APIView
- APIView is the most basic type of view you can use to build your API  
- Enables you to describe logic to make API endpoints; allows us to customize the standard HTTP methods for functions: `GET, POST, PUT, PATCH, and DELETE` 
- Perfect for implementing complex logic, calling other APIs, and working with local files

#### When to use APIViews
- When you need full control over the logic
- Processing files and rendersing a synchronous response 
- When calling other APIs/services
- Accessing local files or data

#### Create first APIView
In `views.py`:
- remove all contents of the file
```
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})
```

#### Explaining the code:
- APIViews are broken up by expecting a function for each HTTP request made to the View; each function is expected to return a response that it will output when the API is called
1. imported standard response object expected to be returned when making an API call, and the APIView class from rest framework.views module 
1. Created a new class based on theAPIView class, allows you to define app logic for the endpoint assigned to this view; defined a endpoint-url and assigned it to this view, Django handles it by calling the correct function in the view for the HTTP request made
1. defined `get` method - retreives a single obj or list of obj; when request is made to the View the logic in the function will execute; The `parameters`: `self` (required for all functions), `request` obj (passed in by DRF and contains details about the request) and `format` used to add a format suffix to the end of the endpoint-URL
1. Defined a list to demonstrate returning an obj in your APIView; DRF expects HTTP functions to return a response obj that will outputted when the API is called. It converts the response obj into JSON; In order to do so the response must contain either a `dictionary {}` or a `list []` 
1. Returned a dictionary; passed in the created list as the value of 'an_apiView' key

#### Configure View URL
- The entry point for all URLS in your app is in a list called `urlpatterns` in the `urls.py` file in the root of the project (created by default when creating a Django project) 
- Example: When heading to `/admin`, Django looks up the `urls.py` file and matches it with the first url it finds. It detects the urls for the admin site which connects that url to the admin app (Django default)
- You can store urls for your API by creating a similar `urls.py` file in the root of your app folder, then including that new `urls.py` file in the `urlpatterns` list of the root project urls

1. `touch profiles_api/urls.py`
1. In `profiles_project/urls.py` 

```
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]
```

#### Explaining the code
1. added include to imports in the project urls, a function used to include urls from other apps
1. added a new path to the list, passed into `include` the app and the module that contains the urls; save. Now the `event loop`: going to `/api` on the server will pass in the request to the django app, which will look into urlpatterns and fin the first item in the list that matches `/api`.  It will then pass in all the urls that match that url and load up the sub urls in `urls.py`. So `/api` is the prefix to the sub-urls.

#### Map A URL to an APIView in Django:
1. In `profiles_api/urls.py`:
```
from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view)
]
```

#### Explaining the code
1. import the path function and the views module which will contain the APIView
1. Created list of paths that map to views: `path('name-of-url', map-to-views.HelloAPIView.call as_view() on the APIViews class)`. 
- Now when the web server address, `/api/hello-view` is accessed, it will call the `views.HelloApiView.as_view()` which is the standard function called to render the appropriate return from the APIView. So making a get request will trigger the get method in the APIView.

#### Test the APIView in the Browser
- `Note`: May need to restart the server
- In Chrome head to trigger the Django Dispatcher: `127.0.0.1:8000/api/hello-view/` to see the output returned from the response of the `views.py` `HelloApi` view

#### Create A Serializer
- A serializer is feaure from the DRF that allows you to easily convert data inputs into python objects and vice-versa
- Similar to Django forms with various fields foro an API
- A serializer is necessary for POST and UPDATE functionality so that we can recieve the content
- Best practice to keep all serializers in one file for easy finding
- serializers also take care of validation rules
1. `touch profiles_api/serializers.py`
1. In 1. `serializers.py`:
```
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializez a name field for testing our APIView"""
    first_name = serializers.CharField(max_length=10)
```

#### Explaining the code
1. Imported serializers from DRF
1. create a new class based on the serializers class in the DRF
1. added a first_name field for testing a POST METHOD


#### Add POST method to APIView
1. In `views.py`:
```
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Returns a list of APIViews features"""
        ...

    def post(self, request):
        """Create a hello message w/ your name"""
        serializer = self.serializer_class(data=request.data)

         if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
         else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST 
                )
            
```

#### Explaining the code
1. Imports: status, a list of handy HTTP status codes you can use when returning responses from the API. Serializers module you created to tell the APIView what data to expect when making PUT, POST, and PATCH requests to the API
1. Set the serialzier; configured the APIView to have the serializer class you created, "When you're sending a POST PUT or PATCH req expect an input with a name that has a max length of 10 characters
1. Write the Post Function that creates a hello message with our name when the API recieves a post request
1. Retrieve the serializer with the `self.serializer_class()` function, which comes w/ the APIView and retreives the configured serialzer class for your view. It's the standard way to retrieve the serializer_class when working with serializers in a view. When making a post request to the API, the data gets passed in as `request.data` (apart of the request object). We assign this data to the serializer class, then created a new variable for the class called `serializer`
1. Validated the serialzer using the is_valid() method off the serialzer class; you can retrieve all fields defined in the serialzer this way
1. Created a message returned from the API that contains the name contained in the post request using f'string {name}' - this lets you insert a variable into a string. This what is returned when a request is valid, if it is not there's the else statement. It is good practice to implement error handling so that those using the API know what went wrong when getting an error.
1. Else return a response (changing to a 400-Bad Request, from the default 200-OK Request) by retrieving the dictionary of errors from the serialzers. Good practice to use the status to return messages so that there is more information.

#### Test Post Function in Browser
1. Head to `/api/hello-view/` and refresh the page to see the name field appear at the bottom due to adding a serializer and post function. Now the API knows we're exepcting a name and gives us a place to input it. See the errors as well.

#### Add Put, PATCH, & DELETE methods
1. In `views.py`:
```
    def put(self, request, pk=None):
        """Handle updating an obj"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an obj"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an obj"""
        return Response({'method': 'DELETE'})
```
- `Note`: When doing a PUT you do it to a specific URL primary key/to a specific ID you are updating. Setting the primary key to `None` is something you can do if you don't want to use primary keys in your API. For now usinf `None`.

#### Test PUT/PATCH/DELETE
- Delete to see the delete response, and likewise for PUT
- For the PATCH method: use `raw` data - we provide only the fields to be updated as a json string in the editor: `{"someKey":"someValue"}`

# 

### 7. Intro to View Sets:

##### Objectives:
- What a Viewset is
- Create a simple viewset
- Add URL Router
- Add create, retrieve, update, partial_update, and destroy functions
- Test Viewset

#### What is a ViewSet
- Similar to views, they help us write logic for endpoints 


























