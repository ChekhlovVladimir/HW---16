import sqlite3
from pprint import pprint as pp

DB_PATH = 'netflix.db'


class NetflixDB:
    def __init__(self, path):
        self.path = path

    def get_data_from_db(self, query):
        """
        Получаем все данные о фильмах из базы данных
        :param query:
        :return: Весь список фильмом с данными
        """
        with sqlite3.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.row_factory = sqlite3.Row
            result = cursor.execute(query).fetchall()

        return result

    def get_element_by_title(self, title):
        """
        Находим фильм или шоу по названию
        :param title: Название
        :return: по указанным полям запроса фильм
        """
        result = self.get_data_from_db(query='''
        SELECT *, MAX(release_year) as max_value 
        FROM netflix
        WHERE type = 'Movie'
        ORDER BY max_value
        
        ''')
        for item in result:
            return item

    def get_elements_by_year(self, from_release_year, to_release_year):
        """
        Для получения картин или шоу по дате их выпуска
        :param from_release_year: диапазон от
        :param to_release_year: диапазон до
        :return: все картины или шоу в этом периоде
        """
        result = self.get_data_from_db(query=f'''
        SELECT title, release_year  
        FROM netflix
        WHERE release_year BETWEEN "{from_release_year}" AND "{to_release_year}"
        AND type = 'Movie'
        ORDER BY release_year
        LIMIT 100
        
        ''')
        if result is not None:
            list_movie = []
            for item in range(len(result)):
                dict_movie = {'title': result[item][0], 'release_year': result[item][1]}
                list_movie.append(dict_movie)
            return list_movie

    def get_elements_by_rating(self, rating_list):
        """
        Получаем картины по возрастному рейтингу
        :param rating_list: список определенных возрастных цензов
        :return: фильмы, соответствующие запросу
        """

        result = self.get_data_from_db(query=f'''
                    SELECT title, rating, description  
                    FROM netflix
                    WHERE rating IN ({str(rating_list)[1:-1]})
                    AND type = 'Movie'
                    ORDER BY rating
                    LIMIT 5''')
        if result is not None:
            list_movie = []
            for item in range(len(result)):
                dict_movie = {'title': result[item][0], 'rating': result[item][1], 'description': result[item][2]}
                list_movie.append(dict_movie)
            return list_movie

    def get_elements_by_genre(self, genre):
        """
        Получаем картины по жанру и выводим новые картины в данном жанре
        :param genre: Любой из списка
        :return: Возвращаем новые фильмы из жанра
        """
        result = self.get_data_from_db(query=f'''
                SELECT title, description, listed_in
                FROM netflix
                WHERE listed_in LIKE '%{genre.title()}%' 
                ORDER BY release_year DESC 
                LIMIT 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

                ''')
        if result is not None:
            list_movie = []
            for item in range(len(result)):
                dict_movie = {'title': result[item][0], 'description': result[item][1], 'listed_in': result[item][2]}
                list_movie.append(dict_movie)
            return list_movie

    def get_elements_by_cast(self, actor1, actor2):
        """
        функцию, которая получает в качестве аргумента имена двух актеров, сохраняет всех актеров из колонки
         cast и возвращает список тех, кто играет с ними в паре больше 2 раз.
        :param actor1: Rose McIver
        :param actor2: Ben Lamb
        :return: Список актеров, игравших более двух раз с этой парой актеров из запроса
        """
        result = self.get_data_from_db(query=f'''
                       SELECT *
                       FROM netflix
                       WHERE "cast" LIKE '%{actor1}%' AND "cast" LIKE '%{actor2}%'
                       LIMIT 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

                       ''')
        if result is not None:
            list_actors = []
            search_results = []
            actors_counts = 0

            for actors in result:
                list_actors.append(dict(actors)['cast'].title().split(", "))
                two_actors = [actor1, actor2]
                list_actors = set(list_actors) - set(two_actors)
                for actor in list_actors:
                    for i in result:
                        if actor in dict(i)['cast']:
                            actors_counts += 1
                    if actors_counts > 2:
                        search_results.append(actor)
            return search_results


db = NetflixDB(DB_PATH)
pp(db.get_elements_by_cast('Rose McIver', 'Ben Lamb'))
