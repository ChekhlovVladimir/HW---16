import sqlite3
from pprint import pprint as pp

DB_PATH = 'netflix.db'


class NetflixDB:
    def __init__(self, path):
        self.path = path

    def get_data_from_db(self, query):
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.row_factory = sqlite3.Row
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

    def get_elements_by_year(self, from_release_year, to_release_year):
        result = self.get_data_from_db(query=f'''
        SELECT title, release_year  
        FROM netflix
        WHERE type = 'Movie'
        GROUP BY title, release_year
        HAVING release_year BETWEEN "{from_release_year}" AND "{to_release_year}"
        ORDER BY release_year
        LIMIT 100
        
        ''')
        for item in result:
            return item


bd = NetflixDB(DB_PATH)
pp(bd.get_elements_by_year(2020, 2021))
