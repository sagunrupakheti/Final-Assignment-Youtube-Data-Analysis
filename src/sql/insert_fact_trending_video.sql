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
