INSERT INTO category(client_category_id,title,assignable)
SELECT DISTINCT(id),title,CAST(assignable AS bool)
FROM raw_category;