import psycopg2
import sqlalchemy
from pprint import pprint

db = 'postgresql://py48galuta:1624@localhost:5432/galutadb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

#название и год выхода альбомов, вышедших в 2018 году;
albom_2018 = connection.execute("""
SELECT name_albom, release_year FROM list_of_albom
WHERE release_year = 2018;
""").fetchall()
print('albom 2018')
print(albom_2018)


# # название и продолжительность самого длительного трека;
mast_long = connection.execute("""
SELECT max(duration_min) FROM list_of_trek;
""").fetchall()
name_mast_long = connection.execute(f"""
SELECT name_trek FROM list_of_trek
WHERE duration_min = {mast_long[0][0]};
""").fetchall()
print(f'''mast long trek {name_mast_long[0][0]},
duration {mast_long[0][0]} min''')


# название треков, продолжительность которых не менее 3,5 минуты;
long_mor_35 = connection.execute("""
SELECT name_trek FROM list_of_trek
WHERE duration_min >= 3.5;
""").fetchall()
print('trek with duration 3.5 min')
print(long_mor_35)

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
colection_18_20 = connection.execute("""
SELECT name_colection FROM list_of_colection
WHERE release_year
BETWEEN 2018 AND 2020;
""").fetchall()
print('colections from 2018 to 2020')
print(colection_18_20)


# исполнители, чье имя состоит из 1 слова;
# name_executor_1_world = connection.execute("""
# SELECT name_executor FROM list_of_executor
# WHERE name_executor NOT
# LIKE "%%""%%" OR "%%""%%""%%";
# """).fetchall()
# print('name only one world')
# print(name_executor_1_world)


# название треков, которые содержат слово "мой"/"my".
# name_executor_1_world = connection.execute("""
# SELECT name_trek FROM list_of_trek
# WHERE name_trek
# LIKE '%%мой%%' OR '%%my%%';
# """).fetchall()
# print('name trek with"мой"/"my"')
# print(name_executor_1_world)



# sel = connection.execute("""
# SELECT * FROM list_of_executor_new;
# """).fetchmany(5)
# print(sel)
#
# sel_a = connection.execute("""
# SELECT date_of_birth FROM list_of_executor_new;
# """).fetchall()
# print(sel_a)
#
# sel_b = connection.execute("""
# SELECT max(id) FROM list_of_executor_new;
# """).fetchall()
# print(sel_b)

