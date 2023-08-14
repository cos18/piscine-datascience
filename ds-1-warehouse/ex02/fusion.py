from sqlalchemy import create_engine
import pandas as pd
import time

start = time.time()
print(f'[{time.time() - start:.2f}s] Start Program')

processed_data = []
engine = create_engine(
    'postgresql://sunpark:mysecretpassword@localhost/piscineds', echo=False)

for chunk in pd.read_sql('select * from customers', engine, chunksize=10**6):
    processed_data.append(chunk)
items_df = pd.read_sql('select * from items', engine)
print(f'[{time.time() - start:.2f}s] Load complete')

customers_df = pd.concat(processed_data).sort_values('event_time')
print(f'[{time.time() - start:.2f}s] Merge & Sort complete')
'''
customers_df.drop_duplicates(['event_type', 'product_id', 'price', 'user_id','user_session'], inplace=True)
print(f'[{time.time() - start:.2f}s] Drop duplicate complete')
customers_df.sort_values('event_time', inplace=True)
print(f'[{time.time() - start:.2f}s] Sort complete')
'''

joined_df = pd.merge(customers_df, items_df, how='left', on='product_id')
print(f'[{time.time() - start:.2f}s] JOIN complete')

joined_df.to_sql('customers',
                 engine,
                 if_exists='replace',
                 index=False,
                 chunksize=10**5)
print(f'[{time.time() - start:.2f}s] ALL complete')
