INSERT INTO dim_category(client_category_id,category_name,assignable)
SELECT client_category_id,title,assignable FROM category