import psycopg2
from tqdm import tqdm
from datetime import timedelta


def check_same(row_a, row_b):
    return row_a[0] == row_b[0] and row_a[1] == row_b[1]\
        and row_a[2] == row_b[2] and row_a[3] == row_b[3]


def ctid_list_to_str(delete_ctid):
    result = '('
    for i in range(len(delete_ctid)):
        result += str(delete_ctid[i])
        if i != len(delete_ctid) - 1:
            result += ','
    result += ')'
    return result


with psycopg2.connect(host='localhost',
                      dbname='piscineds',
                      user='sunpark',
                      password='mysecretpassword') as conn:
    with conn.cursor() as cur:
        print('Calculate distinct users...')
        cur.execute('SELECT DISTINCT user_id FROM customers;')
        users = cur.fetchall()
        for user in tqdm(users, desc='search dup'):
            cur.execute(
                f'SELECT event_time, event_type, product_id, user_session, ctid FROM customers WHERE user_id = {user[0]} ORDER BY event_time;'
            )
            now = cur.fetchall()
            delete_ctid = set()
            for i in range(len(now)):
                for j in range(i + 1, len(now)):
                    if now[i][0] + timedelta(seconds=5) < now[j][0]:
                        break
                    if check_same(now[i], now[j]):
                        delete_ctid.add(now[j][4])
            print(delete_ctid)
            if len(delete_ctid):
                cur.execute(
                    f'DELETE FROM customers WHERE ctid IN {ctid_list_to_str(list(delete_ctid))};'
                )
    conn.commit()
