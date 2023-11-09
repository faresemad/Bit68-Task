# Bit68 Task

## Description

This repository contains a Django application that provides REST API endpoints to manage user registration, login, package management, and subscription functionalities using Django and Django Rest framework. The application is built to work with either PostgreSQL databases. Please follow the instructions below to run the application and access its functionalities.

## Instructions to Run the Code

### 1. Prerequisites:

- Python 3
- Django
- Django Rest framework
- PostgreSQL database

### 2. Clone the repository:

```bash
git clone https://github.com/faresemad/Bit68-Task.git
cd Bit68-Task
```

### 3. Create a virtual environment and install the requirements:

```bash
# Create and activate a virtual environment (optional)
python3 -m venv venv
# For Windows:
venv\Scripts\activate
# For Unix/macOS:
source venv/bin/activate
```

### 4. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 5. Database Configuration:

Create a database in your chosen database system (PostgreSQL).
Update the database settings in `settings.py` to match your database configuration.

### 6. Migrations and Superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 7. Run the Application:

```bash
python manage.py runserver
```

# API Endpoints:

## 1. User Registration:

> Endpoint: /api/register/
> Method: POST
> Description: Register a new user.

## 2.User Login:

> Endpoint: /api/login/
> Method: POST
> Description: Login and obtain an access token.

## 3.Add Package Model:

> Endpoint: Admin panel only.

## 4.Get Packages:

> Endpoint: /api/packages/
> Method: GET
> Description: Get a list of packages, ordered by price and searchable by name.

## 5.Create Subscription:

> Endpoint: /api/subscribe/
> Method: POST
> Description: Make an order with one or more packages.

## 6.Get User Subscriptions:

> Endpoint: /api/user-subscriptions/
> Method: GET
> Description: Retrieve subscriptions for a specific user.

# Additional Features (Optional, as per notes):

## Linting:

> Lint your code using flake8.

## Test Cases:

> Add test cases using pytest or a preferred testing framework.

## Nginx Configuration and Supervisor:

> Set up Nginx configuration and Supervisor for production deployment.

## Deployment:

> Deploy the application on a server.

## Docker and Docker Compose:

> Utilize Docker and Docker Compose for containerization of the application.
