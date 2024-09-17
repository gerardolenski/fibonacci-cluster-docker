import os
import time
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

db_user = os.environ['POSTGRES_USER']
db_password = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB_NAME']
db_host = os.environ['POSTGRES_DB_HOST']

for attempt in range(0,10):
    try:
        con = psycopg2.connect(dbname='postgres',
                               user=db_user, host=db_host,
                               password=db_password)
    except:
        time.sleep(1)
        continue
    else:
        break


cur = con.cursor()
cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", [db_name])
exists = cur.fetchone()
cur.close()

if not exists:
    cur = con.cursor()
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
    cur.close()

con.close()