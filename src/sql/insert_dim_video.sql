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