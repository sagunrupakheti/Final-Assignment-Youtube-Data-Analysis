CREATE TABLE dim_date(
    date_id SERIAL PRIMARY KEY,
    date   date,
    week_day VARCHAR(255)
)