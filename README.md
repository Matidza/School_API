
# Flask Schools API

A RESTful API built with Flask and MongoDB to store and manage data about schools, including their names, addresses, and other details. This API can be used to store data for all schools in a country, providing endpoints for adding, retrieving, updating, and deleting school records.

---

## Features
- **Add School**: Add details about a new school.
- **Retrieve Schools**: Fetch a list of all schools or a specific school by ID.
- **Update School**: Modify details of an existing school.
- **Delete School**: Remove a school record.

---

## Technologies Used
- **Backend Framework**: Flask
- **Database**: MongoDB
- **Python Libraries**: Flask, Flask-PyMongo, BSON

---

## Installation and Setup

### Prerequisites
- Python 3.x installed
- MongoDB server running (local or cloud-based, e.g., MongoDB Atlas)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/schools-api.git
   cd schools-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure MongoDB:
   - Update the MongoDB connection string in `app.py`:
     ```python
     app.config["MONGO_URI"] = "mongodb://localhost:27017/schools_db"
     ```
   - Replace with your MongoDB URI if using a cloud database.

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the API at:
   ```
   http://127.0.0.1:5000
   ```

---

## API Endpoints

### 1. Home
- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Welcome message for the API.
- **Response**:
  ```json
  {
    "message": "Welcome to the Schools API!"
  }
  ```

### 2. Add a New School
- **Endpoint**: `/schools`
- **Method**: `POST`
- **Description**: Add a new school to the database.
- **Request Body**:
  ```json
  {
    "name": "Sunrise High School",
    "address": "123 Main Street",
    "city": "Pretoria",
    "state": "Gauteng",
    "zip_code": "0002"
  }
  ```
- **Response**:
  ```json
  {
    "message": "School added",
    "id": "<new_school_id>"
  }
  ```

### 3. Get All Schools
- **Endpoint**: `/schools`
- **Method**: `GET`
- **Description**: Retrieve a list of all schools.
- **Response**:
  ```json
  [
    {
      "id": "648dfbcbf342a",
      "name": "Sunrise High School",
      "address": "123 Main Street",
      "city": "Pretoria",
      "state": "Gauteng",
      "zip_code": "0002"
    }
  ]
  ```

### 4. Get a Specific School
- **Endpoint**: `/schools/<school_id>`
- **Method**: `GET`
- **Description**: Retrieve details of a specific school by its ID.
- **Response**:
  ```json
  {
    "id": "648dfbcbf342a",
    "name": "Sunrise High School",
    "address": "123 Main Street",
    "city": "Pretoria",
    "state": "Gauteng",
    "zip_code": "0002"
  }
  ```

### 5. Update a School
- **Endpoint**: `/schools/<school_id>`
- **Method**: `PUT`
- **Description**: Update details of an existing school.
- **Request Body**:
  ```json
  {
    "address": "456 Elm Street"
  }
  ```
- **Response**:
  ```json
  {
    "message": "School updated"
  }
  ```

### 6. Delete a School
- **Endpoint**: `/schools/<school_id>`
- **Method**: `DELETE`
- **Description**: Remove a school record by its ID.
- **Response**:
  ```json
  {
    "message": "School deleted"
  }
  ```

---

## Example Usage
### Adding a New School
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"name": "Sunrise High School", "address": "123 Main Street", "city": "Pretoria", "state": "Gauteng", "zip_code": "0002"}' \
http://127.0.0.1:5000/schools
```

### Retrieving All Schools
```bash
curl -X GET http://127.0.0.1:5000/schools
```

---

## License
This project is licensed under the MIT License.

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

Feel free to customize this `README.md` file further based on your repository or project requirements!
