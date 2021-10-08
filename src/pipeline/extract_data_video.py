from establish_connection import connect
from csv import reader
import query
import sql

try:

    def create_raw_video(connection, cursor):
        get_query = sql.open_read_file(query.raw_video_create)
        cursor.execute(get_query)
        connection.commit()

    def insert_into_raw_table(filePath,country,connection,cursor):
        # delete if any data exists in the table
        #https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte
        with open(filePath,'r', encoding = "ISO-8859-1") as file:
            #, encoding = 'utf-8'
            i=0
            for data in reader(file):
                if i==0:
                    i+=1
                    continue
                data.append(str(country))
                #%s to pass the rows
                insert_query = "INSERT INTO raw_video(video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes," \
                               "comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed," \
                               "description,country)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(insert_query,data)
                connection.commit()

    def create_archive_video(connection, cursor):
        get_query = sql.open_read_file(query.archive_video_create)
        cursor.execute(get_query)
        connection.commit()

    def insert_into_archive_table(filePath,country,connection,cursor):
        # delete if any data exists in the table
        #https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte
        with open(filePath,'r', encoding = "ISO-8859-1") as file:
            #, encoding = 'utf-8'
            i=0
            for data in reader(file):
                if i==0:
                    i+=1
                    continue
                data.append(str(country))
                #%s to pass the rows
                insert_query = "INSERT INTO archive_video(video_id,trending_date,title,channel_title,category_id,publish_time,tags,views,likes,dislikes," \
                               "comment_count,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed," \
                               "description,country,filename)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(insert_query,data)
                connection.commit()


    def create_standard_video(connection, cursor):
        get_query = sql.open_read_file(query.standard_video_create)
        cursor.execute(get_query)
        connection.commit()

    def insert_standard_video(connection, cursor):
        delete_table = "TRUNCATE video RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.standard_video_insert)
        cursor.execute(get_query)
        connection.commit()

    def create_dim_country(connection, cursor):
        get_query = sql.open_read_file(query.dim_country_create)
        cursor.execute(get_query)
        connection.commit()

    def load_dim_country(connection, cursor):
        delete_table = "TRUNCATE dim_country RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.dim_country_insert)
        cursor.execute(get_query)
        connection.commit()

    def create_dim_date(connection, cursor):
        get_query = sql.open_read_file(query.dim_date_create)
        cursor.execute(get_query)
        connection.commit()

    def load_dim_date(connection, cursor):
        delete_table = "TRUNCATE dim_date RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.dim_date_insert)
        cursor.execute(get_query)
        connection.commit()

    def create_dim_channel(connection, cursor):
        get_query = sql.open_read_file(query.dim_channel_create)
        cursor.execute(get_query)
        connection.commit()

    def load_dim_channel(connection, cursor):
        delete_table = "TRUNCATE dim_channel RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.dim_channel_insert)
        cursor.execute(get_query)
        connection.commit()

    def create_dim_video(connection, cursor):
        get_query = sql.open_read_file(query.dim_video_create)
        cursor.execute(get_query)
        connection.commit()

    def load_dim_video(connection, cursor):
        delete_table = "TRUNCATE dim_video RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.dim_video_insert)
        cursor.execute(get_query)
        connection.commit()

    def create_fact_trending_video(connection, cursor):
        get_query = sql.open_read_file(query.fact_trending_video_create)
        cursor.execute(get_query)
        connection.commit()

    def load_fact_trending_video(connection, cursor):
        delete_table = "TRUNCATE fact_trending_video RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.fact_trending_video_insert)
        cursor.execute(get_query)
        connection.commit()

    if __name__ == "__main__":
        connection = connect()
        cursor = connection.cursor()
        create_raw_video(connection,cursor)
        print('raw video created')
        insert_into_raw_table('../../data/CAvideos.csv',"Canada",connection,cursor)
        insert_into_raw_table('../../data/DEvideos.csv', "Germany",connection,cursor)
        insert_into_raw_table('../../data/FRvideos.csv', "France",connection,cursor)
        insert_into_raw_table('../../data/GBvideos.csv', "Great Britain",connection,cursor)
        insert_into_raw_table('../../data/INvideos.csv', "India",connection,cursor)
        insert_into_raw_table('../../data/JPvideos.csv', "Japan",connection,cursor)
        insert_into_raw_table('../../data/KRvideos.csv', "Korea",connection,cursor)
        insert_into_raw_table('../../data/MXvideos.csv', "Mexico",connection,cursor)
        insert_into_raw_table('../../data/RUvideos.csv', "Russia",connection,cursor)
        insert_into_raw_table('../../data/USvideos.csv', "United States",connection,cursor)
        print('Inserted into raw')

        create_archive_video(connection,cursor)
        insert_into_archive_table('../../data/CAvideos.csv',"Canada",connection,cursor)
        insert_into_archive_table('../../data/DEvideos.csv', "Germany",connection,cursor)
        insert_into_archive_table('../../data/FRvideos.csv', "France",connection,cursor)
        insert_into_archive_table('../../data/GBvideos.csv', "Great Britain",connection,cursor)
        insert_into_archive_table('../../data/INvideos.csv', "India",connection,cursor)
        insert_into_archive_table('../../data/JPvideos.csv', "Japan",connection,cursor)
        insert_into_archive_table('../../data/KRvideos.csv', "Korea",connection,cursor)
        insert_into_archive_table('../../data/MXvideos.csv', "Mexico",connection,cursor)
        insert_into_archive_table('../../data/RUvideos.csv', "Russia",connection,cursor)
        insert_into_archive_table('../../data/USvideos.csv', "United States",connection,cursor)
        print('Inserted into archive')

        create_standard_video(connection,cursor)
        insert_standard_video(connection,cursor)

        create_dim_country(connection, cursor)
        load_dim_country(connection, cursor)

        create_dim_date(connection, cursor)
        load_dim_date(connection, cursor)

        create_dim_channel(connection, cursor)
        load_dim_channel(connection, cursor)

        print('all data loaded')

        create_dim_video(connection, cursor)
        load_dim_video(connection, cursor)

        create_fact_trending_video(connection, cursor)
        load_fact_trending_video(connection, cursor)


except Exception as e:
    print(e)

