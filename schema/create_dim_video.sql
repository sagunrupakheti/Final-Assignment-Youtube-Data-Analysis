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