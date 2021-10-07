CREATE TABLE dim_category(
    category_id SERIAL PRIMARY KEY,
    client_category_id VARCHAR(255),
    category_name VARCHAR(255),
    assignable bool
)