from flask import jsonify as jsonify
from flask import Flask
from Class import NetflixDB
import json

app = Flask(__name__)
DB_PATH = 'netflix.db'


@app.route('/')
def index_page():
    return "Заполните адресную строку"


@app.route('/movie/<title>', methods=['GET'])
def page_movie(title):
    db = NetflixDB(DB_PATH)
    movie = db.get_element_by_title(title)
    return jsonify(dict(movie))


@app.route('/movie/<int:from_year>/to/<int:to_year>')
def page_movie_by_years(from_year, to_year):
    item_list = []
    db = NetflixDB(DB_PATH)
    movie = db.get_elements_by_year(from_year, to_year)
    for item in movie:
        item_list.append(item)
        return jsonify(dict(item_list))


if __name__ == "__main__":
    app.run(debug=True)
