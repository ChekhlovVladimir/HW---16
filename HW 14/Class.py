import sqlite3
from pprint import pprint as pp


class NetflixDB:
    def __init__(self, path):
        self.path = path

    def get_data_from_db(self, query):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query).fetchall()

        return result

    def get_element_by_title(self, title):
        result = self.get_data_from_db(query='''
        SELECT *, MAX(release_year) as max_value 
        FROM netflix
        WHERE type = 'Movie'
        ORDER BY max_value
        
        ''')
        for item in result:
            return item



