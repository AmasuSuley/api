# Django API Project

## Overview
This is a Django-based API project designed to provide a robust and scalable backend for your application. The API is built using Django REST framework and follows best practices for API development.

## Features
- **User Authentication and Authorization**: Secure user authentication using JWT (JSON Web Tokens).
- **CRUD Operations**: Create, Read, Update, and Delete operations for various models.
- **Pagination, Filtering, and Sorting**: Efficient handling of large datasets with pagination, filtering, and sorting capabilities.
- **Comprehensive Documentation**: Interactive API documentation with Swagger.
- **Unit Tests**: Ensuring code quality and reliability with comprehensive unit tests.

## Requirements
- Python 3.8+
- Django 3.2+
- Django REST framework 3.12+
- PostgreSQL (optional for production)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/AmasuSuley/django-api-project.git
cd django-api-project
```

### 2. Create a Virtual Environment
It's recommended to create a virtual environment to manage dependencies.
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory and add the following environment variables:

```ini name=.env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
# Uncomment and set the following variables for PostgreSQL
# DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

### 6. Run Migrations
Apply the database migrations to set up your database schema.
```bash
python manage.py migrate
```

### 7. Create a Superuser
Create a superuser to access the Django admin interface.
```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
Start the development server.
```bash
python manage.py runserver
```

## Running Tests
To run the tests, use the following command:
```bash
python manage.py test
```

## API Documentation
The API documentation is available at `http://localhost:8000/swagger/` once the server is running. This interactive documentation allows you to explore and test the API endpoints.


## Dependencies
The main dependencies for this project are:
- **Django**: High-level Python web framework.
- **Django REST framework**: Toolkit for building Web APIs.
- **djangorestframework-simplejwt**: For JWT authentication.
- **django-environ**: For environment variable management.
- **drf-yasg**: For generating interactive API documentation.

## Deployment
For deployment, you can use platforms like Heroku, AWS, or any other cloud service. Make sure to configure the environment variables and settings for production.

### Example for Heroku Deployment
1. Install the Heroku CLI.
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```
4. Set environment variables on Heroku:
   ```bash
   heroku config:set SECRET_KEY=your_secret_key
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   heroku config:set DATABASE_URL=postgres://user:password@hostname:5432/dbname
   ```
5. Push your code to Heroku:
   ```bash
   git push heroku main
   ```
6. Run migrations on Heroku:
   ```bash
   heroku run python manage.py migrate
   ```
7. Create a superuser on Heroku:
   ```bash
   heroku run python manage.py createsuperuser
   ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the code style and add tests for new features.

## License
This project is licensed under the MIT License.
