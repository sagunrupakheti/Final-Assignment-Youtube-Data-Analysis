# Data Extraction

---

* Two types of files are given with .json extension and .csv extension
* The json file contains data on categories, and the csv file contains data of trending videos

Steps:

Basics

* .env file containing host, database, user and password information
* establish_connection.py file connecting postgres to psycopg2 using the .env file

~~~python
from dotenv import load_dotenv
load_dotenv()
import os
import psycopg2

def connect():
    return psycopg2.connect(
        user=os.getenv("user"),
        password=os.getenv("password"),
        host=os.getenv("host"),
        port=os.getenv("port"),
        database=os.getenv("database")
    )
~~~

1. Create raw tables raw_category and raw_video

* Similar methods are used to create raw and archive tables
* The sql folder consists of a function that opens a file 
* The query folder consists of variables storing paths of the DDL or DML
* the query is passed into the sql to open the file and the cursor is executed

~~~python
    def create_raw_video(connection, cursor):
        get_query = sql.open_read_file(query.raw_video_create)
        cursor.execute(get_query)
        connection.commit()
~~~

Query for creating raw video table
~~~sql
CREATE TABLE raw_video(
	video_id	VARCHAR(255),
	trending_date	VARCHAR(255),
	title	TEXT,
	channel_title	TEXT,
	category_id	VARCHAR(255),
	publish_time	VARCHAR(255),
	tags	TEXT,
	views	VARCHAR(255),
	likes	VARCHAR(255),
	dislikes	VARCHAR(255),
	comment_count	VARCHAR(255),
	thumbnail_link	TEXT,
	comments_disabled	VARCHAR(255),
	ratings_disabled	VARCHAR(255),
	video_error_or_removed	VARCHAR(255),
	description TEXT,
	country VARCHAR(255)
	);
~~~

Query for creating raw category table
~~~sql
CREATE TABLE raw_category(
	kind VARCHAR(255),
	etag VARCHAR(255),
	id VARCHAR(255),
	channelId VARCHAR(255),
	title VARCHAR(255),
	assignable VARCHAR(255),
	country VARCHAR(255)
)
~~~

2. Create archive tables archive_category and archive_video

Query for creating archive category table
~~~sql
CREATE TABLE archive_category(
	kind VARCHAR(255),
	etag VARCHAR(255),
	id VARCHAR(255),
	channelId VARCHAR(255),
	title VARCHAR(255),
	assignable VARCHAR(255),
	country VARCHAR(255),
	filename TEXT
)
~~~

Query for creating archive video table
~~~sql
CREATE TABLE archive_video(
	video_id	VARCHAR(255),
	trending_date	VARCHAR(255),
	title	TEXT,
	channel_title	TEXT,
	category_id	VARCHAR(255),
	publish_time	VARCHAR(255),
	tags	TEXT,
	views	VARCHAR(255),
	likes	VARCHAR(255),
	dislikes	VARCHAR(255),
	comment_count	VARCHAR(255),
	thumbnail_link	TEXT,
	comments_disabled	VARCHAR(255),
	ratings_disabled	VARCHAR(255),
	video_error_or_removed	VARCHAR(255),
	description TEXT,
	country VARCHAR(255),
	filename TEXT
	);
~~~

3. Extract data into raw and archive tables 

To insert into raw category table,
* The json file is opened
* Looped through items dictionary
* Each value individually pulled and inserted
* The raw table only contains country not filename
~~~python
            for category in data['items']:
                id_to_category[category['id']] = category['snippet']['title'],category['snippet']['assignable']
                category_list = [category['kind'],\
                        category['etag'],category['id'],category['snippet']['channelId'],category['snippet']['title'],
                                 category['snippet']['assignable'],country,filename]
                cursor.execute(open_file,category_list)
                connection.commit()
~~~

To insert into raw video table,
* The csv file opened
* The header is skipped
* Country is appended to each row and data is inserted for each country
~~~python
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
~~~