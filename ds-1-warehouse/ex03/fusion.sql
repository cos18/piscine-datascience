CREATE TEMPORARY TABLE temp_item AS
SELECT
    product_id,
    COALESCE(MAX(category_id), NULL) AS category_id,
    COALESCE(MAX(category_code), NULL) AS category_code,
    COALESCE(MAX(brand), NULL) AS brand
FROM
    item
GROUP BY
    product_id;

TRUNCATE item;
INSERT INTO item SELECT * FROM temp_item;

CREATE TEMPORARY TABLE temp_customers AS
SELECT
    customers.*,
    item.category_id,
    item.category_code,
    item.brand
FROM customers LEFT JOIN item ON customers.product_id=item.product_id;

TRUNCATE customers;
ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code TEXT,
ADD COLUMN brand TEXT;
INSERT INTO customers SELECT * FROM temp_customers;
