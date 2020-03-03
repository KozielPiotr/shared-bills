# Shared bills

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a web application to share costs of event between many participants.
Let's say you go on a trip with your friends. Someone pays for car, another one for food, someone else for tickets. In this app you can just create event and connect bills to it, assign participants, set participant who pays for this bill and take a look who owns who money and how much.
	
## Technologies
Project is created with:
* backend:
  * Python 3
  * Django 3
  * Django REST Framework
* frontend:
  * TypeScript
  * ReactJS
  * RxJS
	
## Setup
To run this project locally:
* backend (with dummy SECRET_KEY):
  * Linux:
    ```
    $ export SECRET_KEY="dummy"
    ```
  * Windows:
    ```
    $ set SECRET_KEY="dummy"
    ```
  ```
  $ pip install -r requirements.txt
  $ python manage.py migrate
  $ python manage.py runserver
  ```
  You can also create superuser account:
  ```
  $ python manage.py createsuperuser
  ```
* frontend
  ```
  $ cd frontend
  $ npm install
  $ npm start
  ```
