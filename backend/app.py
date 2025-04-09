from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
# Enable CORS for all routes and origins
CORS(app)

# Connection to the database
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host='database'
    )
    return conn

# Main page GET, getting all tasks from the database
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, description, completed FROM tasks ORDER BY id')
    tasks = [{'id': t[0], 'description': t[1], 'completed': t[2]} for t in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(tasks)

# Route to add a new task to the database
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    description = data['description']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (description) VALUES (%s)', (description,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Task added'}), 201

# Route to update a task state in the database
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def toggle_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('UPDATE tasks SET completed = NOT completed WHERE id = %s', (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Task updated'})

# Route to delete a task from the database
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Task deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)