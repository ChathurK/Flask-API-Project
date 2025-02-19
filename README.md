# README.md

# Flask API Project

This project is a simple Flask API that allows for user management with CRUD operations. It uses Flask-SQLAlchemy for database interactions and PyMySQL as the MySQL driver.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/ChathurK/Flask-API-Project.git
   cd api
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   Ensure that you have a MySQL server running and create a database named `flask_api_db`.

5. **Run the application**:
   ```
   python app.py
   ```

## Usage

- **Home Route**: Access the home route at `http://localhost:5000/` to see a welcome message.
- **User Management**:
  - **Get all users**: `GET /users`
  - **Get a single user**: `GET /users/<user_id>`
  - **Add a new user**: `POST /users` with JSON body `{"name": "User Name", "email": "user@example.com"}`
  - **Update an existing user**: `PUT /users/<user_id>` with JSON body `{"name": "New Name", "email": "newemail@example.com"}`
  - **Delete a user**: `DELETE /users/<user_id>`

## Dependencies

- Flask
- Flask-SQLAlchemy
- PyMySQL

## License

This project is licensed under the MIT License.