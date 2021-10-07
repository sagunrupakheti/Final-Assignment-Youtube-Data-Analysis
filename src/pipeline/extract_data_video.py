from establish_connection import connect
from csv import reader
import query
import sql
try:

    def insert_into_raw_table(filePath,country):
        connection = connect()
        cursor = connection.cursor()
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

    if __name__ == "__main__":
        #insert_into_raw_table('../../data/CAvideos.csv',"Canada")
        #insert_into_raw_table('../../data/DEvideos.csv', "Germany")
        #insert_into_raw_table('../../data/FRvideos.csv', "France")
        #insert_into_raw_table('../../data/GBvideos.csv', "Great Britain")
        #insert_into_raw_table('../../data/INvideos.csv', "India")
        #insert_into_raw_table('../../data/JPvideos.csv', "Japan")
        #insert_into_raw_table('../../data/KRvideos.csv', "Korea")
        #insert_into_raw_table('../../data/MXvideos.csv', "Mexico")
        #insert_into_raw_table('../../data/RUvideos.csv', "Russia")
        insert_into_raw_table('../../data/USvideos.csv', "United States")
except Exception as e:
    print(e)

