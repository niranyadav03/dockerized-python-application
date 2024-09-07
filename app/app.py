from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId

# Initialize the Flask app
app = Flask(__name__)

# MongoDB connection setup
client = MongoClient('mongodb://mongo:27017/')
db = client.todo_db
todos_collection = db.todos

# Route to serve the HTML UI
@app.route('/')
def index():
    return render_template('index.html')

# Route to get all to-do tasks (API)
@app.route('/todos', methods=['GET'])
def get_all_todos():
    todos = []
    for todo in todos_collection.find():
        todos.append({
            'id': str(todo['_id']),
            'task': todo['task'],
            'status': todo['status']
        })
    return jsonify(todos)

# Route to create a new to-do task (API)
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = {
        'task': data.get('task'),
        'status': 'incomplete'
    }
    result = todos_collection.insert_one(new_todo)
    return jsonify({'id': str(result.inserted_id)}), 201

# Route to update a to-do task (API)
@app.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
    data = request.json
    updated_todo = {
        'task': data.get('task'),
        'status': data.get('status')
    }
    result = todos_collection.update_one({'_id': ObjectId(id)}, {'$set': updated_todo})
    if result.matched_count:
        return jsonify({'message': 'Task updated successfully'})
    return jsonify({'message': 'Task not found'}), 404

# Route to delete a to-do task (API)
@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    result = todos_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return jsonify({'message': 'Task deleted successfully'})
    return jsonify({'message': 'Task not found'}), 404

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
