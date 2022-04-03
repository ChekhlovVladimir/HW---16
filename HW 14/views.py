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
    db = NetflixDB(DB_PATH)
    movie = db.get_elements_by_year(from_year, to_year)
    return jsonify(movie)


@app.route('/rating/<classified_rating>')
def page_movie_by_rating(classified_rating):
    db = NetflixDB(DB_PATH)
    rating_list = []
    if classified_rating == 'children':
        rating_list = ['G']
    elif classified_rating == 'family':
        rating_list = ['G', 'PG', 'PG-13']
    elif classified_rating == 'adult':
        rating_list = ['R', 'NC-17']

    result = db.get_elements_by_rating(rating_list)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
