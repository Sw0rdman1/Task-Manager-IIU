from flask import Flask, jsonify, request
from flask_cors import CORS
import database


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    database.initalConnectToDB()
    return 'Hello World!'


@app.route('/tasks')
def get_all_tasks():
    # Returning an api for showing in  reactjs
    return jsonify(database.getAllTasksFromDB())


@app.route('/tasks/update', methods=['POST'])
def update_task():
        request_data = request.get_json()  # parse request body as JSON

        database.updateTaskInDB(request_data)

        return 'Task updated'


@app.route('/tasks/create', methods=['POST'])
def create_task():
        request_data = request.get_json()  # parse request body as JSON
        database.addTaskToDB(request_data)

        return jsonify(database.getAllTasksFromDB())

@app.route('/tasks/delete', methods=['DELETE'])
def delete_task():
        request_data = request.get_json()  # parse request body as JSON
        print(request_data)
        database.deleteTaskFromDB(request_data)

        return jsonify(database.getAllTasksFromDB())



if __name__ == '__main__':
    app.run()
