# Load Data
 
Steps:
1. Create fact and dimension tables

* Similar methods are used to create other dimension and fact tables
* The sql folder consists of a function that opens a file 
* The query folder consists of variables storing paths of the DDL or DML query as per requirement
~~~python
    
    def create_dim_category(connection,cursor):
        get_query = sql.open_read_file(query.dim_category_create)
        cursor.execute(get_query)
        connection.commit()
~~~

Query to create dimension category
~~~sql
CREATE TABLE dim_category(
    category_id SERIAL PRIMARY KEY,
    client_category_id VARCHAR(255),
    category_name VARCHAR(255),
    assignable bool
)
~~~
Query to create dimension channel
~~~sql
CREATE TABLE dim_channel(
    channel_id SERIAL PRIMARY KEY,
    channel_title TEXT
)
~~~
Query to create dimension country
~~~sql
CREATE TABLE dim_country(
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255)
)
~~~
Query to create dimension date
~~~sql
CREATE TABLE dim_date(
    date_id SERIAL PRIMARY KEY,
    date   date,
    week_day VARCHAR(255)
)
~~~
Query to create dimension video
~~~sql
CREATE TABLE dim_video(
    id SERIAL PRIMARY KEY,
	client_video_id	VARCHAR(255),
	category_id INT,
	channel_id INT,
	title	TEXT,
	publish_date DATE,
	publish_time time,
	tags TEXT,
    title_word_count INT,
    tags_count INT,
    has_special_character bool
	);
~~~
Query to create fact trending video 
~~~sql
CREATE TABLE fact_trending_video(
    video_id INT NOT NULL,
    country_id INT NOT NULL,
    date_id INT NOT NULL,
    views INT NOT NULL,
    likes INT NOT NULL,
    dislikes INT NOT NULL,
    comment_count INT NOT NULL,
    days_after_publish INT NOT NULL,
    PRIMARY KEY(video_id,country_id,date_id),
    CONSTRAINT fk_video FOREIGN KEY(video_id) REFERENCES dim_video(id),
    CONSTRAINT fk_country FOREIGN KEY(country_id) REFERENCES dim_country(country_id),
    CONSTRAINT fk_date FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
)
~~~

2. Insert into fact and dimension tables from standard tables

* Similar functions are used to insert 
* The method for extraction is full extraction thus, each table 
  needs to be cleaned prior to insertion
* The sql folder consists of a function that opens a file 
* The query folder consists of variables storing paths of the DDL or DML
* the query is passed into the sql to open the file and the cursor is executed
~~~python 
    def insert_dim_category(connection,cursor):
        delete_table = "TRUNCATE dim_category RESTART IDENTITY CASCADE;"
        cursor.execute(delete_table)
        get_query = sql.open_read_file(query.dim_category_insert)
        cursor.execute(get_query)
        connection.commit()
~~~
Query to insert into dimension category
~~~sql
INSERT INTO dim_category(client_category_id,category_name,assignable)
SELECT client_category_id,title,assignable FROM category
~~~
Query to insert into dimension channel
* Only the channel names of most recently added video information is stored to avoid inconsistent reference
~~~sql
INSERT INTO dim_channel(channel_title)
with max_val_vid as(select max(id) AS max from video v GROUP BY client_video_id),
get_all as (SELECT * from max_val_vid,video where id=max_val_vid.max )
select distinct(channel_title) from get_all;
~~~
Query to insert into dimension country
~~~sql
INSERT INTO dim_country(country_name)
SELECT DISTINCT(country) FROM video
~~~
Query to insert into dimension date
* Only unique trending dates are stored
~~~sql
INSERT INTO dim_date(date,week_day)
SELECT
DISTINCT trending_date ,
to_char(trending_date, 'Day')
FROM video
~~~
Query to insert into dimension video
* A slowly changing dimension (SCD) type 1 is implemented where only the recent data is stored
* Video information of most recently added video is only stored
* Video id remains consistent
* Tags and Title are stored as list separated by a comma
* Checked if title has any special character
~~~sql
INSERT INTO dim_video(client_video_id,category_id,channel_id,title,publish_date,publish_time,tags,title_word_count,
tags_count,has_special_character)
with get_max as(select max(id) AS max from video v GROUP BY client_video_id),
all_vid as (SELECT * from get_max,video where id=get_max.max )
SELECT
client_video_id,
(SELECT category_id FROM dim_category c WHERE x.category_id= c.client_category_id),
(SELECT channel_id FROM dim_channel c WHERE x.channel_title= c.channel_title),
title,
publish_date,
publish_time,
tags,
array_length(string_to_array(title,' '),1),
array_length(string_to_array(tags,','),1),
CASE WHEN title LIKE ANY (array['%!%', '%.%', '%-%','%|%','%#%','%?%','%,%']) THEN true ELSE false END
from all_vid x;
~~~
Query to insert into fact trending video
* The videos are group as one unique video per day per country
* Necessary foreign keys are added which form a composite key
~~~sql
INSERT INTO fact_trending_video(video_id,country_id,date_id,views,likes,dislikes,comment_count,days_after_publish)
with get_max as(select max(id) AS max from video v GROUP BY client_video_id,country,trending_date),
all_vid as (SELECT * from get_max,video where id=get_max.max )
SELECT
(SELECT v.id FROM dim_video v WHERE v.client_video_id= a.client_video_id),
(SELECT country_id FROM dim_country c WHERE c.country_name = a.country),
(SELECT date_id FROM dim_date d WHERE d.date = a.trending_date),
views,
likes,
dislikes,
comment_count,
trending_date-publish_date
from all_vid a ;
~~~