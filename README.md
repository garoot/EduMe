# EduMe E-learning Platform
The files in this project are intended for the development team. In this README doc, I will layout the steps to setup the project. EduMe is built using Django framework.

## Setup Guide
First, you need to install Django. Please follow the steps in the link below up until step 4, "Install Django in Mac":
https://appdividend.com/2018/03/28/how-to-install-django-in-mac/#Step_4Install_Django_In_Mac

You don't have to create a new Django project since we already have one. In the terminal:
- Go to EduMe/ folder 
- source activate nameOfEnvironment
#### The next two steps only do them when you first setup the project, and when you make changes to models.py and admins.py
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- copy the link to the development server an paste it on your browser

