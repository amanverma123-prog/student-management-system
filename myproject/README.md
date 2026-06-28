# Student Management System

A web application built with Django and MySQL to manage student records.

## Features
- User Authentication (Login, Logout, Signup)
- Add, Edit, Delete, View Students
- Search Students by Name
- MySQL Database Integration
- Responsive UI with Bootstrap

## Tech Stack
- Python
- Django
- MySQL
- Bootstrap 5
- HTML/CSS

## Setup Instructions

1. Clone the repository
git clone https://github.com/amanverma123-prog/student-management-system.git

2. Install dependencies
pip install -r requirements.txt

3. Copy settings example
cp myproject/settings_example.py myproject/settings.py

4. Update database credentials in `settings.py`

5. Run migrations
python manage.py migrate

6. Create superuser
python manage.py createsuperuser

7. Run server
python manage.py runserver

8. Open browser at `http://127.0.0.1:8000/students/`
