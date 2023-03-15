from flask import Flask, request, jsonify
import random

app = Flask(__name__)


class User:
    def __init__(self, email, firstname, id):
        self.email = email
        self.firstname = firstname
        self.id = id


listOfUsers = []
user1 = User("abc@abc.ca", "ABC", "5abf6783")
user2 = User("xyz@xyz.ca", "XYZ", "5abf674563")

listOfUsers.append(user1)
listOfUsers.append(user2)


@app.route('/users', methods=['GET'])
def initalGet():
    return jsonify({'message': 'Users retrieved', 'success': True, 'users': [ob.__dict__ for ob in listOfUsers]})


@app.route('/update/<id>', methods=['PUT'])
def putData(id):
    data = request.get_json()
    email = data.get('email')
    firstName = data.get('firstName')
    for obj in listOfUsers:
        if obj.id == id:
            obj.firstname = firstName
            obj.email = email
            return jsonify({'message': 'User updated', 'success': True})
        else:
            return jsonify({'message': 'User updated', 'success': False})


@app.route('/add', methods=['POST'])
def postData():
    data = request.get_json()
    email = data.get('email')
    firstName = data.get('firstName')
    id = random.randint(1, 10)
    user = User(email, firstName, id)
    listOfUsers.append(user)

    return jsonify({'message': 'User added', 'success': True})


@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = User("", "", "")
    for obj in listOfUsers:
        if obj.id == id:
            user = obj
            return jsonify({'success': True, 'user': user.__dict__})
        else:
            return jsonify({'success': False})


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
