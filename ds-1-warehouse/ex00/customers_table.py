import psycopg2
import time

month_dic = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12
}


def db_key(db_str: str) -> int:
    result = 0
    lst = db_str.split('_')
    try:
        result += int(lst[1])
    except:
        result += 9999
    result *= 13
    try:
        result += int(month_dic[lst[2]])
    except:
        pass
    return result


start = time.time()

# Around 5 min to run
with psycopg2.connect(host='localhost',
                      dbname='piscineds',
                      user='sunpark',
                      password='mysecretpassword') as conn:
    with conn.cursor() as cur:
        cur.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_name LIKE 'data_%_%' AND table_schema = 'public';"
        )
        db_list = list(cur.fetchall())
        db_list.sort(key=lambda db: db_key(db[0]))
        print(db_list)
        cur.execute('DROP TABLE IF EXISTS public.customers;')
        cur.execute('''CREATE TABLE IF NOT EXISTS public.customers
                        (
                            event_time TIMESTAMP with time zone,
                            event_type TEXT,
                            product_id INT,
                            price NUMERIC,
                            user_id BIGINT,
                            user_session CHAR(36)
                        );''')
        for db in db_list:
            db_start = time.time()
            cur.execute(
                f'INSERT INTO customers SELECT event_time, event_type, product_id, price, user_id, user_session FROM {db[0]}'
            )
            print(
                f'Insert {db[0]} to customers complete : {time.time() - db_start} sec'
            )
    conn.commit()

print(f'total time : {time.time() - start}')
