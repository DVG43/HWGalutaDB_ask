import psycopg2
import sqlalchemy
from pprint import pprint

db = 'postgresql://py48galuta:1624@localhost:5432/galutadb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# # количество исполнителей в каждом жанре;
# qwontat_exec_in_gener = connection.execute("""
# SELECT COUNT(id),name_gener FROM list_of_gener lg
# JOIN list_executors_and_geners leg ON lg.id = leg.id_geners
# GROUP BY id;
# """).fetchall()
# print ('(n исполнителей, жанр)')
# print(qwontat_exec_in_gener)
#
#
# # количество треков, вошедших в альбомы 2002-2008 годов;
# qwontat_trek_in_albom = connection.execute("""
# SELECT  name_trek, id_albom FROM list_of_trek lt
# FULL OUTER JOIN list_of_albom lal ON lt.id_albom = lal.id
# WHERE release_year BETWEEN 2002 AND 2008;
# """).fetchall()
# print ('количество треков с 2002 по 2008')
# print(len(qwontat_trek_in_albom))
#
#
# # средняя продолжительность треков по каждому альбому;
# avereg_duration_in_albom = connection.execute("""
# SELECT  name_albom, AVG(duration_min) FROM list_of_trek lt
# FULL OUTER JOIN list_of_albom lal ON lt.id_albom = lal.id
# GROUP BY  name_albom;
# """).fetchall()
# print ('средняя продолжительность треков по альбомам')
# pprint (avereg_duration_in_albom)

# все исполнители, которые не выпустили альбомы в 2020 году;


# названия сборников, в которых присутствует конкретный исполнитель (vasia petrov);
# avereg_duration_in_albom = connection.execute("""
# SELECT  name_colection  FROM list_of_colection lc
# JOIN list_treck_and_colection ltc ON lc.id = ltc.id_colection
# JOIN list_of_trek lt ON ltc.id_treck = lt.id
# JOIN list_of_albom lal ON lt.id_albom = lal.id
# JOIN list_executors_and_albom leal ON lal.id = leal.id_albom
# JOIN list_of_executor le ON leal.id_executor = le.id
# WHERE name_executor = 'vasia petrov';
# """).fetchall()
# print ('названия сборников, в которых присутствует vasia petrov')
# pprint (avereg_duration_in_albom)



# название альбомов, в которых присутствуют исполнители более 1 жанра;
name_albom_with_exekt_muligener = connection.execute("""
SELECT id_geners, name_albom, name_executor FROM list_of_albom lal
JOIN list_executors_and_albom lea ON lal.id = lea.id_albom
JOIN list_of_executor le1 ON lea.id_executor = le1.id
JOIN list_executors_and_geners leg ON le1.id = leg.id_executor

""").fetchall()
print ('название альбомов, в которых присутствуют исполнители более 1 жанра')
pprint (name_albom_with_exekt_muligener)
#     GROUP BY id_geners, name_albom,
# HAVING COUNT(id_geners) >= 2;

# HAVING COUNT (id_geners) >=2
# наименование треков, которые не входят в сборники; сделать список сборник_трек,
# потом пройти по нему циклом и по результату NULL выявить интересный нам.


# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
#групировка по минималке

# название альбомов, содержащих наименьшее количество треков