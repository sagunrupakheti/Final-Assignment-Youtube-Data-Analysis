INSERT INTO dim_channel(channel_title)
with max_val_vid as(select max(id) AS max from video v GROUP BY client_video_id),
get_all as (SELECT * from max_val_vid,video where id=max_val_vid.max )
select distinct(channel_title) from get_all;