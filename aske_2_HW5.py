import psycopg2
import sqlalchemy
from pprint import pprint

db = 'postgresql://py48galuta:1624@localhost:5432/galutadb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# количество исполнителей в каждом жанре;
qwontat_exec_in_gener = connection.execute("""
SELECT COUNT(id),name_gener FROM list_of_gener lg
JOIN list_executors_and_geners leg ON lg.id = leg.id_geners
GROUP BY id;
""").fetchall()
print ('(n исполнителей, жанр)')
print(qwontat_exec_in_gener)

# количество исполнителей в каждом жанре;
# фильмы, которые берут в прокат чаще всего
# con.execute("""
# SELECT id,name_gener COUNT(r.inventory_id) count FROM film f
# JOIN inventory i ON f.film_id = i.film_id
# JOIN rental r ON i.inventory_id = r.inventory_id
# GROUP BY f.title
# ORDER BY count DESC;
# """).fetchall()
#
#
# con.execute("""
# SELECT store_id, city, country FROM store s
# JOIN address a ON s.address_id = a.address_id
# JOIN city ON a.city_id = city.city_id
# JOIN country c ON city.country_id = c.country_id;
# """).fetchall()

# количество треков, вошедших в альбомы 2019-2020 годов;


# средняя продолжительность треков по каждому альбому;


# все исполнители, которые не выпустили альбомы в 2020 году;


# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);


# название альбомов, в которых присутствуют исполнители более 1 жанра;


# наименование треков, которые не входят в сборники;


# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);


# название альбомов, содержащих наименьшее количество треков