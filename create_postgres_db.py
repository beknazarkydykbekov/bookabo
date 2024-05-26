import psycopg2
from psycopg2 import sql

"""
You can update the DB variables to your liking
"""

DB_NAME = "bookabo_db"
DB_USER = "beknazarkydykbekov"
DB_PASSWORD = "ksfnskfi39893c33"
DB_HOST = "localhost"
DB_PORT = "5432"

conn = psycopg2.connect(dbname="postgres", user=DB_USER, password="beka2002mu",
                        host=DB_HOST, port=DB_PORT)

conn.autocommit = True
cursor = conn.cursor()

cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (DB_NAME,))
db_exists = cursor.fetchone()

if not db_exists:
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
    print(f"Database {DB_NAME} created successfully.")
else:
    print(f"Database {DB_NAME} already had been created.")

cursor.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", (DB_USER,))
user_exists = cursor.fetchone()

if not user_exists:
    cursor.execute(sql.SQL("CREATE USER {} WITH PASSWORD %s").format(sql.Identifier(DB_USER)), [DB_PASSWORD])
    print(f"User {DB_USER} created successfully.")
else:
    print(f"User {DB_USER} already had been created.")

cursor.execute(sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(sql.Identifier(DB_NAME),
                                                                           sql.Identifier(DB_USER)))
print(f"Granted all privileges on {DB_NAME} to {DB_USER}.")

cursor.close()
conn.close()
