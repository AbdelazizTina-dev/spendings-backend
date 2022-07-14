Django RESTful API for Daily Spendings

# How to start it:
- Install the latest Python version.

- Install Django:

  `$ python -m pip install Django`

- Install Django REST Framework:

  `$ pip install djangorestframework`
  
- Install Django REST Framework:

  `$ python -m pip install django-cors-headers`
  
- Apply migrations:

  `$ python manage.py migrate`
  
- Start the application:

  `$ python manage.py runserver`
  
# API endpoints:

## GET:
- Get spendings list: `\spendings`
- Get a specific spending by id: `\spendings\id`

## POST:
- Post a new spending: `\spendings`

## PUT:
- Update an existing spending: `\spendings\id`

## DELETE:
- Delete a spending: `\spendings\id`
