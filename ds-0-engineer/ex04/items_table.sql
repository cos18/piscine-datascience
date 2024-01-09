DROP TABLE IF EXISTS public.items;

CREATE TABLE IF NOT EXISTS public.items
(
    product_id    INT,
    category_id   BIGINT,
    category_code TEXT,
    brand         TEXT
);

COPY items(product_id, category_id, category_code, brand)
FROM '/var/lib/postgresql/goinfre/item/item.csv'
DELIMITER ','
CSV HEADER;

COPY items(product_id, category_id, category_code, brand)
TO '/var/lib/postgresql/goinfre/export/items/items.csv'
DELIMITER ',' CSV HEADER;