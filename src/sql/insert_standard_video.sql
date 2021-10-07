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