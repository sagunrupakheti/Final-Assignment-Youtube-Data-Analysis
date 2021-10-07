##Transform Data

Steps:
1. Create standard tables category and video

~~~sql
CREATE TABLE category(
	category_id SERIAL PRIMARY KEY,
	client_category_id VARCHAR(255),
	title TEXT,
	assignable bool
)
~~~

~~~sql

CREATE TABLE video(
	id SERIAL PRIMARY KEY,
	client_video_id VARCHAR(255),
	trending_date date,
	title TEXT,
	channel_title TEXT,
	category_id VARCHAR(255),
	publish_date DATE,
	publish_time time,
	tags TEXT,
	views INT,
	likes INT,
	dislikes INT,
	comment_count INT,
	country VARCHAR(255)
)
~~~

2. Transform and insert into standard category table

~~~sql
INSERT INTO category(client_category_id,title,assignable)
SELECT DISTINCT(id),title,CAST(assignable AS bool)
FROM raw_category;
~~~
* distinct categories, their title and assignable value

3. Transform and insert into standard video table

~~~sql
INSERT INTO video(client_video_id,trending_date,title,channel_title,category_id,publish_date,publish_time,tags,views,
likes,dislikes,comment_count,country)
SELECT
video_id,
TO_DATE(trending_date ,'YY-DD-MM'),
title,channel_title,category_id,
TO_TIMESTAMP(split_part(publish_time,'T',1),'YYYY-MM-DD HH24:MI:SS')::date,
CAST(TRIM(TRAILING '.000Z' FROM split_part(publish_time,'T',2)) as time),
replace(replace (tags, '"', ''),'|',','),
views,likes,dislikes,comment_count,country
FROM raw_video WHERE video_id <> '#NAME?' AND video_id <> '#VALUE!';
~~~