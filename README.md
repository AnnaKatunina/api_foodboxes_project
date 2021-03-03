# Django REST API project

This application displays a prototype of API service for shipping foodboxes sets.
The application accepts GET requests and returns a response in the following format:
```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "title": "Дачник",
    "description": "Ваш огородный урожай в одной коробке",
    "image": "https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/static/foodb4.jpg",
    "weight": 2300,
    "price": "850.00"
}
```
____
## Requirements

- Python 3.7+
- Django 3.1

## Installing

1\. Clone the repository
```
git clone https://github.com/AnnaKatunina/api_foodboxes_project.git
```
2\. Create and activate virtualenv
- for Linux/macOS
```
python -m venv venv
source venv/bin/activate
```
- for Windows
```
python -m venv venv
venv\Scripts\activate
```
3\. Install packages from requirements.txt
```
pip install -r requirements.txt
```
## Usage

Run the application
```
python manage.py runserver
```
Open your web browser and enter the URL displayed in the terminal:
- http://127.0.0.1:8000/api/v1/items/<item_id> or http://localhost:8000/api/v1/items/<item_id>
- http://127.0.0.1:8000/api/v1/users/<user_id> or http://localhost:8000/api/v1/users/<user_id>
- http://127.0.0.1:8000/api/v1/reviews/<review_id> or http://localhost:8000/api/v1/reviews/<review_id>