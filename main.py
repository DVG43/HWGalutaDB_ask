import psycopg2
import sqlalchemy
from pprint import pprint
#import json


def change_str_to_int(any_list, namber_member):
   some_value = any_list[namber_member]
   any_list.pop(namber_member)
   our_list = []
   for elem in any_list:
       our_list.append(int(elem))
   our_list.insert(namber_member, some_value)
   return  our_list


class Table:
    def __init__(self, quant_col):
        self.quant_col = quant_col


    def data_entry(self,namber_text_columnn):
        #finish_list = []
        current_list = []
        marker = input('хотите ввести строку таблицы y or n ?')
        while marker == 'y':
           current_string_list = input('строка?').split(',')
           if len(current_string_list) != self.quant_col:
                print('ошибка ввода')
           index = namber_text_columnn - 1
           some_new_list = change_str_to_int(current_string_list, index)
           current_list.append(some_new_list)
           marker1 = input('хотите ввести строку таблицы y or n ?')
           marker = marker1
        return current_list

def get_tuple_for_bd ():
    quant_columns = int(input("введите количество колонок"))
    namber_t_col = int(input("введите номер текстовой колонки"))
    table = Table(quant_columns)
    table_of_data = table.data_entry(namber_t_col)
    table_of_tuple = [tuple(element) for element in table_of_data]
    return table_of_tuple


if __name__ == '__main__':

    db = 'postgresql://py48galuta:1624@localhost:5432/galutadb'
    engine = sqlalchemy.create_engine(db)
    connection = engine.connect()
    print("Сейчас вы будете вводить лист жанров ")
    geners = get_tuple_for_bd()
    pprint(geners)
    for str_tabl in geners:
        connection.execute(f"""
        INSERT INTO list_of_gener(id,name_gener)VALUES{str_tabl};
        """)

    # не    менее    8    исполнителей
    print("""Сейчас вы будете вводить лист исполнителей
    id,name_executor,date_of_birth""")
    executors = get_tuple_for_bd()
    pprint(executors)
    for str_tabl_a in executors:
        connection.execute(f"""
        INSERT INTO list_of_executor(id,name_executor,date_of_birth)
        VALUES{str_tabl_a};
        """)

    # не менее 8 альбомов;
    print("""Сейчас вы будете вводить лист альбомовй
    id,name_albom,release_year,id_executor""")
    alboms = get_tuple_for_bd()
    pprint(alboms)
    for str_tabl_b in alboms:
        connection.execute(f"""
        INSERT INTO list_of_albom(id,name_albom,release_year,id_executor)
        VALUES{str_tabl_b};
        """)


    # не менее 15 треков;
    print("""С""ейчас вы будете вводить лист треков
    id,name_trek,duration_min,id_albom""")
    treks = get_tuple_for_bd()
    pprint(treks)
    for str_tabl_c in treks:
        connection.execute(f"""
        INSERT INTO list_of_trek(id,name_trek,duration_min,id_albom)
        VALUES{str_tabl_c};
        """)


    # не менее 8 сборников.
    print("""Сейчас вы будете вводить лист сборников
    id,name_colection,release_year """)
    colections = get_tuple_for_bd()
    pprint(colections)
    for str_tabl_d in colections:
        connection.execute(f"""
         INSERT INTO list_of_colection(id,name_colection,release_year)
         VALUES{str_tabl_d};
         """)


    # связь исполнителей и жанров.
    print("""Сейчас вы будете вводить лист связи исполнителей и жанров
    id_geners,id_executor """)
    exec_gener = get_tuple_for_bd()
    pprint(exec_gener)
    for str_tabl_e in exec_gener:
        connection.execute(f"""
         INSERT INTO list_executors_and_geners(id_geners,id_executor)
         VALUES{str_tabl_e};
         """)

    # связь альбомов и исполнителей.
    print("""Сейчас вы будете вводить лист связи альбомов и исполнителей
    id_albom,id_executor """)
    exec_alb = get_tuple_for_bd()
    pprint(exec_alb)
    for str_tabl_g in exec_alb:
        connection.execute(f"""
         INSERT INTO list_executors_and_albom(id_albom,id_executor)
         VALUES{str_tabl_g};
         """)


    # связь треков и колекций.
    print("""Сейчас вы будете вводить лист связи треков и колекций
    id_treck,id_colection """)
    trek_col = get_tuple_for_bd()
    pprint(trek_col)
    for str_tabl_i in trek_col:
        connection.execute(f"""
         INSERT INTO list_treck_and_colection(id_treck,id_colection)
         VALUES{str_tabl_i};
         """)


# Внимание! Должны быть заполнены все поля каждой таблицы, в т.ч. таблицы связей
# (исполнителей с жанрами, исполнителей с альбомами, сборников с треками).

