from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = '../database/activity_tracking.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Welcome to the Activity Metrics API!"

@app.route('/metrics/static', methods=['GET'])
def static_metrics():
    # Example of a static endpoint
    conn = get_db_connection()
    metrics = conn.execute('SELECT * FROM PerformanceMetrics LIMIT 10').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in metrics])

@app.route('/metrics/<activity_id>', methods=['GET'])
def dynamic_metrics(activity_id):
    # Example of a dynamic endpoint
    conn = get_db_connection()
    metrics = conn.execute('SELECT * FROM PerformanceMetrics WHERE ActivityID = ?', (activity_id,)).fetchall()
    conn.close()
    if metrics:
        return jsonify([dict(ix) for ix in metrics])
    else:
        return jsonify({"error": "Activity not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
