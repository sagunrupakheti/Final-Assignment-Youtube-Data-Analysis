from establish_connection import connect

try:

    def insert_table_dim_fact(filePath):
        source_conn = connect()
        dest_conn = connect()

        source_cursor = source_conn.cursor()
        dest_cursor = dest_conn.cursor()

        with open(filePath) as file:
            sql = "".join(file.readlines())
            source_cursor.execute(sql)
            result = source_cursor.fetchall()
            sql = 'INSERT INTO fact_trending_video(video_id,country_id,date_id,views,likes,dislikes,comment_count,days_after_publish)' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
            for row in result:
                dest_cursor.execute(sql,row)
                dest_conn.commit()


    if __name__ == "__main__":
        #insert_table_dim_fact('../sql/insert_dim_category.sql')
        #insert_table_dim_fact('../sql/insert_dim_country.sql')
        #insert_table_dim_fact('../sql/insert_dim_date.sql')
        #insert_table_dim_fact('../sql/insert_dim_channel.sql')
        #insert_table_dim_fact('../sql/insert_dim_video.sql')
        insert_table_dim_fact('../sql/insert_fact_trending_video.sql')

except Exception as e:
    print(e)