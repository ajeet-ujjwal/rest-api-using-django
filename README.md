# rest-api-using-django

This project was built using Python, Django and Django Rest Framework. Database SQLite is used to retain the data.

**Python version 3.6.4**

## Steps to Run

```
# Clone the project
git clone https://github.com/ajeet-ujjwal/rest-api-using-django.git

# Install python 3.6.4

# Create virtual environment 
python3 -m venv <env_name>

# Install dependencies after activating virtual environment 
pip install -r requirements.txt

# Create Database Tables
python manage.py migrate

# Run Django Server
python manage.py runserver

```

## Features and API Endpoints

Feature | Api Endpoint
------------ | -------------
Retrieve all vessels  | GET 127.0.0.1:8000/vessels/
Retrieve a vessel | GET 127.0.0.1:8000/vessels/:id
Create a new vessel | POST 127.0.0.1:8000/vessels/
Update a vessel | PUT 127.0.0.1:8000/vessels/:id
Delete a vessel | DELETE 127.0.0.1:8000/vessels/:id

## Testing
To run all unit tests, run the command: python manage.py test




