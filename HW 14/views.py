from flask import jsonify as jsonify
from flask import Flask
from Class import NetflixDB
import json

app = Flask(__name__)
DB_PATH = 'netflix.db'


@app.route('/')
def index_page():
    return " Заполните адресную строку"


@app.route('/movie/<title>', methods=['GET'])
def page_movie(title):
    db = NetflixDB(DB_PATH)
    movie = db.get_element_by_title(title)
    for item in movie:
        return jsonify(title=item['title'],
                       country=item['country'],
                       release_year=item['release_year'],
                       genre=item['listed_in'],
                       description=item['description'])


if __name__ == "__main__":
    app.run(debug=True)
