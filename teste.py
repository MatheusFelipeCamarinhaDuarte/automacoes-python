import psycopg2
try:

    conn1 = psycopg2.connect(
        port='5432',
        host="localhost",
        user='postgres',
        password='postgres',
        database='banco_teste'
    )
    cur1 = conn1.cursor()
except:
    print('nãoconsegue')