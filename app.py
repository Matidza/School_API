from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/schools_db"  # Replace with your MongoDB URI
mongo = PyMongo(app)
schools_collection = mongo.db.schools

# Helper function to format MongoDB documents
def format_school(school):
    return {
        "id": str(school["_id"]),
        "name": school["name"],
        "address": school["address"],
        "city": school["city"],
        "state": school["state"],
        "zip_code": school["zip_code"],
    }

# Routes

# Home
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Schools API!"}), 200

# Add a new school
@app.route("/schools", methods=["POST"])
def add_school():
    data = request.json
    if not all(k in data for k in ("name", "address", "city", "state", "zip_code")):
        return jsonify({"error": "Missing required fields"}), 400

    new_school = {
        "name": data["name"],
        "address": data["address"],
        "city": data["city"],
        "state": data["state"],
        "zip_code": data["zip_code"],
    }
    result = schools_collection.insert_one(new_school)
    return jsonify({"message": "School added", "id": str(result.inserted_id)}), 201

# Get all schools
@app.route("/schools", methods=["GET"])
def get_schools():
    schools = list(schools_collection.find())
    return jsonify([format_school(school) for school in schools]), 200

# Get a specific school by ID
@app.route("/schools/<school_id>", methods=["GET"])
def get_school(school_id):
    school = schools_collection.find_one({"_id": ObjectId(school_id)})
    if not school:
        return jsonify({"error": "School not found"}), 404
    return jsonify(format_school(school)), 200

# Update a school
@app.route("/schools/<school_id>", methods=["PUT"])
def update_school(school_id):
    data = request.json
    update_data = {key: value for key, value in data.items() if key in ("name", "address", "city", "state", "zip_code")}

    if not update_data:
        return jsonify({"error": "No valid fields to update"}), 400

    result = schools_collection.update_one({"_id": ObjectId(school_id)}, {"$set": update_data})
    if result.matched_count == 0:
        return jsonify({"error": "School not found"}), 404
    return jsonify({"message": "School updated"}), 200

# Delete a school
@app.route("/schools/<school_id>", methods=["DELETE"])
def delete_school(school_id):
    result = schools_collection.delete_one({"_id": ObjectId(school_id)})
    if result.deleted_count == 0:
        return jsonify({"error": "School not found"}), 404
    return jsonify({"message": "School deleted"}), 200

# Run the app
if __name__ == "__main__":
    app.run(debug=True)


    """
    # Database Confifguration
app.config['MONGO_URI']=  MONGO_URI #os.environ.get('MONGODB_URI')

# Connect app to the database
mongo = PyMongo(app)

# DB Schema of the API
school_schema = {
    "name": str,
    "address": str
}


@app.route('/schools', methods= ['GET'])
def schools():
    schools = mongo.db.schools.find()
    return jsonify([school_schema for school in schools])

@app.route('/schools', methods = ['POST'])
def create_school():
    data = request.get_json()
    if not data:
        return jsonify({"error": "ïnvalid request"}), 400
    school = {
        "name": data['name'],
        "address": data['address']
    }
    mongo.db.schools.insert_one(school)
    return jsonify({"message": "School create Successfully!"}), 201

    """