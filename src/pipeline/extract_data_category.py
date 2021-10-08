#imports
import json
from lxml import etree
from establish_connection import connect
import query
import sql

try:
    def create_table_raw_category():
        connection = connect()
        cursor = connection.cursor()
        get_query = sql.open_read_file(query.raw_category_create)
        cursor.execute(get_query)
        connection.commit()

    #insert from json file
    def insert_table_raw_json(filename,country):
        connection = connect()
        cursor = connection.cursor()
        id_to_category = {}

        with open(filename, 'r') as f:
            data = json.load(f)
            category_list=[]
            for category in data['items']:
                id_to_category[category['id']] = category['snippet']['title'],category['snippet']['assignable']
                category_list = [category['kind'],\
                        category['etag'],category['id'],category['snippet']['channelId'],category['snippet']['title'],
                                 category['snippet']['assignable'],country]
                query = 'INSERT INTO raw_category(kind,etag,id,channelId,title,assignable,country)VALUES(%s,%s,%s,%s,%s,%s,%s);'
                cursor.execute(query,category_list)
                connection.commit()

    def create_table_archive_category():
        connection = connect()
        cursor = connection.cursor()
        get_query = sql.open_read_file(query.archive_category_create)
        cursor.execute(get_query)
        connection.commit()

    def insert_archive_json(filename,country):
        connection = connect()
        cursor = connection.cursor()
        id_to_category = {}
        open_file = sql.open_read_file(query.archive_category_insert)
        with open(filename, 'r') as f:
            data = json.load(f)
            category_list=[]
            for category in data['items']:
                id_to_category[category['id']] = category['snippet']['title'],category['snippet']['assignable']
                category_list = [category['kind'],\
                        category['etag'],category['id'],category['snippet']['channelId'],category['snippet']['title'],
                                 category['snippet']['assignable'],country,filename]
                cursor.execute(open_file,category_list)
                connection.commit()

    def create_standard_category(connection,cursor):
        get_query = sql.open_read_file(query.standard_category_create)
        cursor.execute(get_query)
        connection.commit()

    def insert_standard_category(connection,cursor):
        delete_table = "TRUNCATE category RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.standard_category_insert)
        cursor.execute(get_query)
        connection.commit()

    def create_dim_category(connection,cursor):
        get_query = sql.open_read_file(query.dim_category_create)
        cursor.execute(get_query)
        connection.commit()

    def insert_dim_category(connection,cursor):
        delete_table = "TRUNCATE dim_category RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.dim_category_insert)
        cursor.execute(get_query)
        connection.commit()

    if __name__ == "__main__":
        connection = connect()
        cursor = connection.cursor()
        create_table_raw_category()
        insert_table_raw_json('../../data/US_category_id.json','United States')
        insert_table_raw_json('../../data/DE_category_id.json', 'Germany')
        insert_table_raw_json('../../data/FR_category_id.json', 'France')
        insert_table_raw_json('../../data/GB_category_id.json', 'Great Britain')
        insert_table_raw_json('../../data/IN_category_id.json', 'India')
        insert_table_raw_json('../../data/JP_category_id.json', 'Japan')
        insert_table_raw_json('../../data/KR_category_id.json', 'Korea')
        insert_table_raw_json('../../data/CA_category_id.json', 'Canada')
        insert_table_raw_json('../../data/MX_category_id.json', 'Mexico')
        insert_table_raw_json('../../data/RU_category_id.json', 'Russia')
        print('All raw inserted')
        create_table_archive_category()
        insert_archive_json('../../data/US_category_id.json','United States')
        insert_archive_json('../../data/DE_category_id.json', 'Germany')
        insert_archive_json('../../data/FR_category_id.json', 'France')
        insert_archive_json('../../data/GB_category_id.json', 'Great Britain')
        insert_archive_json('../../data/IN_category_id.json', 'India')
        insert_archive_json('../../data/JP_category_id.json', 'Japan')
        insert_archive_json('../../data/KR_category_id.json', 'Korea')
        insert_archive_json('../../data/CA_category_id.json', 'Canada')
        insert_archive_json('../../data/MX_category_id.json', 'Mexico')
        insert_archive_json('../../data/RU_category_id.json', 'Russia')
        print('All archive inserted')

        create_standard_category(connection,cursor)
        insert_standard_category(connection,cursor)
        create_dim_category(connection,cursor)
        insert_dim_category(connection,cursor)
        print('all done')

        connection.commit()

except Exception as e:
    print(e)