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