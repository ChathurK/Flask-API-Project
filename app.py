from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MYsql2023#@localhost/flask_api_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

# Create the database tables
with app.app_context():
    db.create_all()

""" # Sample data (in-memory storage)
users = [] """

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API"}), 200

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    if not users:
        return jsonify({"message": "No users found"}), 200
    return jsonify(users), 200

# Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if "name" in data:
        user["name"] = data["name"]
    if "email" in data:
        user["email"] = data["email"]

    return jsonify(user), 200

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
