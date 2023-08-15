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
time_log(start, 'Load complete')

customers_df = pd.concat(processed_data)
time_log(start, 'Merge complete')

customers_df.drop_duplicates(
    ['event_type', 'product_id', 'price', 'user_id', 'user_session'],
    inplace=True)
time_log(start, 'Drop duplicate complete')
customers_df.sort_values('event_time', inplace=True)
time_log(start, 'Sort complete')

customers_df.to_csv('/goinfre/sunpark/data/customers_no_dup.csv', index=False)

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
    user_session CHAR(36)
);''')
        time_log(start, 'CREATE')

        cur.execute(
            '''COPY customers(event_time, event_type, product_id, price, user_id, user_session)
                        FROM '/var/lib/postgresql/goinfre/customers_no_dup.csv'
                        DELIMITER ','
                        CSV HEADER;''')
        time_log(start, 'COPY')
    conn.commit()
time_log(start, 'END')

'''
[0.00s] Start Program
[0.03s] Start Program
[642.83s] Load complete
[645.94s] Merge complete
[664.53s] Drop duplicate complete
[666.48s] Sort complete
[766.27s] DROP
[766.29s] CREATE
[1038.63s] COPY
[1038.85s] END
'''
