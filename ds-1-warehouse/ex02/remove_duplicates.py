from sqlalchemy import create_engine
import pandas as pd
import time

processed_data = []
start = time.time()
engine = create_engine(
    'postgresql://sunpark:mysecretpassword@localhost/piscineds', echo=False)
print(f'[{time.time() - start:.2f}s] Start Program')

for chunk in pd.read_sql('select * from customers', engine, chunksize=10**6):
    processed_data.append(chunk)
print(f'[{time.time() - start:.2f}s] Chunk complete')

customers_df = pd.concat(processed_data)
print(f'[{time.time() - start:.2f}s] Merge complete')

customers_df.drop_duplicates(
    ['event_type', 'product_id', 'price', 'user_id', 'user_session'],
    inplace=True)
print(f'[{time.time() - start:.2f}s] Drop duplicate complete')
customers_df.sort_values('event_time', inplace=True)
print(f'[{time.time() - start:.2f}s] Sort complete')
customers_df.to_sql('customers',
                    engine,
                    if_exists='replace',
                    index=False,
                    chunksize=10**6)
print(f'[{time.time() - start:.2f}s] ALL complete')
