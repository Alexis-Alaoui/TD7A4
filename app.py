import os
import time
from flask import Flask
from pymongo import MongoClient
from flask import jsonify


# Create a Flask application instance
app = Flask(__name__)

# Connect to the MongoDB container
# We use the hostname "mongodb" to connect to the MongoDB container
# as it will be automatically resolved to the IP address of the container
# within the Docker network
client = MongoClient("my-mongo")

# Get a reference to the test_database
db = client.mydb
collection=db.mycollection

posts = [    { "nom": "Laura Llinares", "age": 22, "profession": "Développeur" },    
         { "nom": "Karim Benzema", "age": 34, "profession": "Ballon d'or" },    
         { "nom": "Jolyane Mak", "age": 8, "profession": "Doctor" },
         { "nom": "Timothé", "age": 21, "profession": "Chomeur" }]

collection.insert_many(posts)


@app.route("/")
def hello():
    # Fetch a single document from the test_collection
    data = [
    {key: str(value) if key == "_id" else value for key, value in d.items()}
    for d in collection.find()
]
    # Return the fetched data as a string
    return jsonify(data)


def read_file():
    with open("/app/TEST.txt", "r") as file:
        return file.read()

@app.route('/td6')
def hello_world():
    content = read_file()
    return f'Hello, World! Here is the content of the file: {content}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
