
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
