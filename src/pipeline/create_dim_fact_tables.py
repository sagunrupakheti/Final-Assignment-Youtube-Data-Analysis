from establish_connection import connect

try:

    def create_table_dim_fact(filePath):
        connection = connect()
        cursor = connection.cursor()
        with open(filePath) as file:
            sql = "".join(file.readlines())
            cursor.execute(sql)
            connection.commit()


    if __name__ == "__main__":
        #create_table_dim_fact('../../schema/create_dim_category.sql')
        #create_table_dim_fact('../../schema/create_dim_country.sql')
        #create_table_dim_fact('../../schema/create_dim_date.sql')
        #create_table_dim_fact('../../schema/create_dim_channel.sql')
        #create_table_dim_fact('../../schema/create_dim_video.sql')
        create_table_dim_fact('../../schema/create_fact_trending_video.sql')

except Exception as e:
    print(e)