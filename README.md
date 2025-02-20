# Flask API Project

This project is a simple **Flask API** that allows for **user management with CRUD operations**.  
It uses **Flask-SQLAlchemy** for database interactions and **PyMySQL** as the MySQL driver.

## 🚀 Features
- RESTful API for user management
- CRUD operations (Create, Read, Update, Delete)
- Uses **Flask-SQLAlchemy** for database handling
- MySQL as the database backend
- Easy setup with virtual environment and dependency management

---

## 🛠 Setup Instructions

### 1️⃣ Clone the repository
```sh
git clone https://github.com/ChathurK/Flask-API-Project.git
cd Flask-API-Project
```

### 2️⃣ Create a virtual environment (Recommended)
```sh
python -m venv venv # Activate the virtual environment:

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

### 4️⃣ Set up the database
Ensure that you have a MySQL server running, then create a database:
```sh
CREATE DATABASE flask_api_db;
```
Update the database connection settings in app.py if needed.

### 5️⃣ Run the application
```sh
python app.py
```
By default, the Flask server will start at http://localhost:5000/.

---

## 📌 API Endpoints

## 🌍 Home Route
- GET / → Returns a welcome message.

### 👤 User Management
| Action            | Method  | Endpoint             | Request Body (JSON)                                 |
|-------------------|---------|----------------------|-----------------------------------------------------|
| Get all users     | `GET`   | `/users`             | -                                                   |
| Get single user   | `GET`   | `/users/<user_id>`   | -                                                   |
| Add new user      | `POST`  | `/users`             | `{"name": "John Doe", "email": "john@example.com"}` |
| Update user       | `PUT`   | `/users/<user_id>`   | `{"name": "Jane Doe", "email": "jane@example.com"}` |
| Delete user       | `DELETE`| `/users/<user_id>`   | -                                                   |


---
---

## 📦 Dependencies

This project requires the following Python packages:
```sh
blinker==1.9.0
click==8.1.8
colorama==0.4.6
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
greenlet==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.5
MarkupSafe==3.0.2
PyMySQL==1.0.2
SQLAlchemy==2.0.38
typing_extensions==4.12.2
Werkzeug==3.1.3
```
If you need to update or add new dependencies, use:
```sh
pip freeze > requirements.txt
```

---

## 📌 Notes

If you encounter issues with venv, ensure that you have Python installed and pip updated:
```sh
python -m pip install --upgrade pip
```
- Ensure MySQL is running before starting the API.
- Modify database credentials inside app.py to match your MySQL setup.