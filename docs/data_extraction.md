##Data Extraction

---

* Two types of files are given with .json extension and .csv extension
* The json file contains data on categories, and the csv file contains data of trending videos

Steps:

1. Create raw tables raw_category and raw_video
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

* For category:
~~~python
            for category in data['items']:
                id_to_category[category['id']] = category['snippet']['title'],category['snippet']['assignable']
                category_list = [category['kind'],\
                        category['etag'],category['id'],category['snippet']['channelId'],category['snippet']['title'],
                                 category['snippet']['assignable'],country,filename]
                cursor.execute(open_file,category_list)
                connection.commit()
~~~

* For video:

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