DROP TABLE IF EXISTS public.data_2022_oct;

CREATE TABLE IF NOT EXISTS public.data_2022_oct
(
    event_time TIMESTAMP with time zone,
    event_type TEXT,
    product_id INT,
    price NUMERIC,
    user_id BIGINT,
    user_session CHAR(36)
);

COPY data_2022_oct(event_time, event_type, product_id, price, user_id, user_session)
FROM '/var/lib/postgresql/goinfre/subject/customer/data_2022_oct.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS public.data_2022_nov;

CREATE TABLE IF NOT EXISTS public.data_2022_nov
(
    event_time TIMESTAMP with time zone,
    event_type TEXT,
    product_id INT,
    price NUMERIC,
    user_id BIGINT,
    user_session CHAR(36)
);

COPY data_2022_nov(event_time, event_type, product_id, price, user_id, user_session)
FROM '/var/lib/postgresql/goinfre/subject/customer/data_2022_nov.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS public.data_2022_dec;

CREATE TABLE IF NOT EXISTS public.data_2022_dec
(
    event_time TIMESTAMP with time zone,
    event_type TEXT,
    product_id INT,
    price NUMERIC,
    user_id BIGINT,
    user_session CHAR(36)
);

COPY data_2022_dec(event_time, event_type, product_id, price, user_id, user_session)
FROM '/var/lib/postgresql/goinfre/subject/customer/data_2022_dec.csv'
DELIMITER ','
CSV HEADER;

DROP TABLE IF EXISTS public.data_2023_jan;

CREATE TABLE IF NOT EXISTS public.data_2023_jan
(
    event_time TIMESTAMP with time zone,
    event_type TEXT,
    product_id INT,
    price NUMERIC,
    user_id BIGINT,
    user_session CHAR(36)
);

COPY data_2023_jan(event_time, event_type, product_id, price, user_id, user_session)
FROM '/var/lib/postgresql/goinfre/subject/customer/data_2023_jan.csv'
DELIMITER ','
CSV HEADER;