from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

tasks = []

@main.route('/tasks', methods=['POST'])
def create_task():
    task = request.get_json()
    task['id'] = len(tasks) + 1
    tasks.append(task)
    return jsonify(task), 201

@main.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@main.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)

@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    data = request.get_json()
    task.update(data)
    return jsonify(task)

@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return '', 204