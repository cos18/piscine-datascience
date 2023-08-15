import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import time


def time_log(start, log):
    print(f'[{time.time() - start:.2f}s] {log}')


start = time.time()
time_log(start, 'Start Program')

processed_data = []
engine = create_engine(
    'postgresql://sunpark:mysecretpassword@localhost/piscineds', echo=False)

for chunk in pd.read_sql('select * from customers', engine, chunksize=10**6):
    processed_data.append(chunk)
items_df = pd.read_sql('select * from items', engine)
items_df['category_id'] = items_df['category_id'].fillna(0).astype(
    'int64').map(lambda x: str(x) if x else '')
time_log(start, 'Load complete')

customers_df = pd.concat(processed_data).sort_values('event_time')
time_log(start, 'Merge & Sort complete')
'''
customers_df.drop_duplicates(['event_type', 'product_id', 'price', 'user_id','user_session'], inplace=True)
time_log(start, 'Drop duplicate complete')
customers_df.sort_values('event_time', inplace=True)
time_log(start, 'Sort complete')
'''

joined_df = pd.merge(customers_df, items_df, how='left', on='product_id')
time_log(start, 'JOIN complete')

joined_df.to_csv('/goinfre/sunpark/data/join.csv', index=False)
time_log(start, 'Save to CSV File')

with psycopg2.connect(host='localhost',
                      dbname='piscineds',
                      user='sunpark',
                      password='mysecretpassword') as conn:
    with conn.cursor() as cur:
        cur.execute('DROP TABLE IF EXISTS public.customers;')
        time_log(start, 'DROP')

        cur.execute('''CREATE TABLE IF NOT EXISTS public.customers
(
    event_time TIMESTAMP with time zone,
    event_type TEXT,
    product_id INT,
    price NUMERIC,
    user_id BIGINT,
    user_session CHAR(36),
    category_id   BIGINT,
    category_code TEXT,
    brand         TEXT
);''')
        time_log(start, 'CREATE')

        cur.execute(
            '''COPY customers(event_time, event_type, product_id, price, user_id, user_session, category_id, category_code, brand)
                        FROM '/var/lib/postgresql/goinfre/join.csv'
                        DELIMITER ','
                        CSV HEADER;''')
        time_log(start, 'COPY')
    conn.commit()
'''
[0.00s] Start Program
[104.56s] Load complete
[108.58s] Merge & Sort complete
[121.27s] Drop duplicate complete
[122.90s] Sort complete
[135.00s] JOIN complete
[386.08s] Save to CSV File
[386.18s] DROP
[386.20s] CREATE
[1097.72s] COPY
'''
