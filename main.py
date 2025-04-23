
import os
import time
import subprocess
import psycopg2

from etl.extract import load_json
from etl.transform import normalize_data
from etl.load import insert_all

def start_postgres_container():
    print("Starting PostgreSQL container...")
    subprocess.run(["docker", "compose", "-f", "docker/docker-compose.yml", "up", "-d"], check=True)
    print("Waiting for PostgreSQL to be ready...")
    time.sleep(10)

def create_tables(conn, schema_file="db/schema.sql"):
    print("Creating tables from schema.sql...")
    with open(schema_file, "r") as f:
        sql = f.read()
    with conn.cursor() as cur:
        cur.execute(sql)
    conn.commit()
    print("Tables created.")

def main():
    start_postgres_container()

    print("Connecting to database...")
    for _ in range(5):
        try:
            conn = psycopg2.connect(
                dbname="computers_db",
                user="admin",
                password="admin",
                host="localhost",
                port="5432"
            )
            break
        except Exception:
            print("Retrying connection...")
            time.sleep(3)
    else:
        raise Exception("Failed to connect to PostgreSQL.")

    create_tables(conn)

    print("Running ETL process...")
    raw_data = load_json("data/raw_computers.json")
    normalized = normalize_data(raw_data)
    insert_all(conn, normalized)
    conn.close()

    print("Pipeline complete.")

if __name__ == "__main__":
    main()
