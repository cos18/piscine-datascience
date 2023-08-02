import psycopg2

# TODO: COPY 쿼리를 이용한 파일 처리로 변환이 필요
with psycopg2.connect(host='localhost',
                      dbname='piscineds',
                      user='sunpark',
                      password='mysecretpassword') as conn:
    with conn.cursor() as cur:
        cur.execute('''
SELECT table_name
FROM information_schema.tables
WHERE table_name LIKE 'data_%_%' AND table_schema = 'public';
        ''')
        db_list = list(cur.fetchall())
        db_query = '\nUNION\nSELECT event_time, event_type, product_id, price, user_id, user_session FROM '.join(
            [db[0] for db in db_list])
        cur.execute(f'''
CREATE TABLE customers
AS
SELECT event_time, event_type, product_id, price, user_id, user_session FROM {db_query};
        ''')
    conn.commit()
