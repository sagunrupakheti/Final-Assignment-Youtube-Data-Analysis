INSERT INTO dim_date(date,week_day)
SELECT
DISTINCT trending_date ,
to_char(trending_date, 'Day')
FROM video