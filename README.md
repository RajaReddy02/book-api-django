# 📘 Book API – Django REST Framework Project

This is a full-featured backend project built with **Django** and **Django REST Framework**. It provides a token-authenticated API for users to register, log in, and manage books and categories.

---

## 🚀 Features

- 🔐 User Registration & Login with Token Auth
- 📚 CRUD operations for Books
- 🗂️ Category management
- 👥 Authenticated API access
- 🔁 Nested Serializers
- 🛠️ Built with Django, DRF, SQLite

---

## 🧱 Tech Stack

- Python 3
- Django 4+
- Django REST Framework
- SQLite (default DB)

---

## 📁 Project Structure

```text
book-api/
├── books/         # App: Book & Category logic
│   ├── models.py
│   ├── views.py
│   └── serializers.py
├── users/         # App: User Registration & Login
│   ├── views.py
│   └── urls.py
├── bookapi/       # Project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3     # Default database (created after migrations)
├── manage.py      # Django management script
├── requirements.txt

```

---

## 🔧 Setup Instructions

```bash
# 1. Clone the project
git clone https://github.com/your-username/book-api-django.git
cd book-api-django

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Migrate database
python manage.py makemigrations
python manage.py migrate

# 5. Run server
python manage.py runserver
```
---

## 📮 API Endpoints
🔑 User Authentication
| Method | Endpoint               | Description         |
| ------ | ---------------------- | ------------------- |
| POST   | `/api/users/register/` | Register new user   |
| POST   | `/api/users/login/`    | Login and get token |


📝 Login Request Example:
```text


{
  "username": "raja1234",
  "password": "rr"
}
```

🧾 Authorization Header (for all protected endpoints):

Authorization: Token your_token_here

---

## 📚 Book & Category Management

| Method | Endpoint                 | Description            | Auth Required |
| ------ | ------------------------ | ---------------------- | ------------- |
| GET    | `/api/books/`            | List all books         | ✅ Yes         |
| POST   | `/api/books/`            | Create new book        | ✅ Yes         |
| GET    | `/api/books/{id}/`       | Retrieve a single book | ✅ Yes         |
| PUT    | `/api/books/{id}/`       | Update a book          | ✅ Yes         |
| DELETE | `/api/books/{id}/`       | Delete a book          | ✅ Yes         |
| GET    | `/api/books/categories/` | List all categories    | ✅ Yes         |
| POST   | `/api/books/categories/` | Create a new category  | ✅ Yes         |

---

## 📝 Example Book POST Payload:
```text

{
  "title": "Django for APIs",
  "author": "William S. Vincent",
  "published_date": "2023-01-10",
  "category": {
    "name": "Programming"
  }
}
```

---

## 🧪 Testing
You can test this API using:

-🧰 Postman

-🖥️ curl commands

-🧪 Swagger UI (optional if added)

---

## 📌 Author
Raja Reddy Nalamolu
🔗 [LinkedIn Profile](https://www.linkedin.com/in/raja-reddy-nalamolu-14a512230)
