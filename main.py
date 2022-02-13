import psycopg2
import sqlalchemy
from pprint import pprint
import json


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
    # cursor = connection.cursor()
    print("Сейчас вы будете вводить лист жанров ")
    geners = get_tuple_for_bd()
    pprint(geners)
    connection.executemany('''INSERT INTO list_of_gener VALUES (?,?)''', geners)

# connection.execute("""INSERT INTO rental(rental_date, inventory_id, customer_id, staff_id)
#            VALUES(NOW(), 1, 3, 2);
