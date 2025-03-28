# Django API Project

## Overview
This project is a Django-based API service. It is deployed on AWS.

## Technologies Used
- Python
- Django
- Django REST Framework
- AWS (EC2, S3, RDS, etc.)

## Prerequisites
- Python 3.x
- Django 3.x or later
- AWS account
- AWS CLI configured

## Installation

### Clone the repository
```bash
git clone https://github.com/AmasuSuley/api.git
cd api
```

### Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
python manage.py migrate
```

### Create a superuser
```bash
python manage.py createsuperuser
```

### Start the development server
```bash
python manage.py runserver
```

## Deployment on AWS

### 1. Set up an EC2 Instance

1. Go to the AWS Management Console.
2. Launch a new EC2 instance with the desired configuration.
3. SSH into your EC2 instance.

### 2. Install Dependencies on EC2

```bash
sudo apt update
sudo pip3 install virtualenv
```

### 3. Clone the Project on EC2

```bash
git clone https://github.com/AmasuSuley/api.git
cd api
```

### 4. Set up the Virtual Environment and Install Dependencies

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```



## Running Tests

To run tests, use the following command:
```bash
python manage.py test
```

