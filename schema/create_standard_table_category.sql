CREATE TABLE category(
	category_id SERIAL PRIMARY KEY,
	client_category_id VARCHAR(255),
	title TEXT,
	assignable bool
)