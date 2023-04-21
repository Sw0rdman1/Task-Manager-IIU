from flask import Flask, jsonify, request
from database import init_app, create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/tasks'

init_app(app)


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/tasks', methods=['POST'])
def create_task_controller():
    title = request.json.get('title')
    description = request.json.get('description')
    done = request.json.get('done', False)
    task = create_task(title=title, description=description, done=done)
    return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}), 201

@app.route('/tasks', methods=['GET'])
def get_all_tasks_controller():
    tasks = get_all_tasks()
    result = []
    for task in tasks:
        result.append({'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done})
    return jsonify(result), 200


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task_controller(id):
    task = get_task_by_id(id)
    done = request.json.get('done')
    task = update_task(task, done=done)
    return jsonify(),200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task_controller(id):
    task = get_task_by_id(id)
    tasks = delete_task(task)
    result = []
    for task in tasks:
        result.append({'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done})
    return jsonify(result), 200
