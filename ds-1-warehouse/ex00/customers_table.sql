DROP TABLE IF EXISTS public.customers;

CREATE TABLE IF NOT EXISTS public.customers
(
    event_time TIMESTAMP with time zone,
    event_type TEXT,
    product_id INT,
    price NUMERIC,
    user_id BIGINT,
    user_session CHAR(36)
);

select table_name
from information_schema.tables
where table_name like 'data_%_%'
      and table_schema = 'public';