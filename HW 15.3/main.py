import sqlite3
from flask import Flask, jsonify

from config import DB_PATH
from queries import GET_ANIMAL_BY_ID

app = Flask(__name__)


def serialization(row: sqlite3.Row):
    return dict(row)


@app.route('/<id>')
def get_animal_by_id(id):
    conn: sqlite3.Connection = app.config['db']
    cursor = conn.cursor()
    cursor.execute(GET_ANIMAL_BY_ID, (id, ))

    row = cursor.fetchone()
    cursor.close()
    return jsonify(serialization(row))


if __name__ == '__main__':

    connection = sqlite3.connect(DB_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    app.config['db'] = connection
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        connection.close()
