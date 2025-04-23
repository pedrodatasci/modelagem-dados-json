
def insert_data(conn, table, data):
    if not data:
        return
    keys = data[0].keys()
    columns = ', '.join(keys)
    placeholders = ', '.join(['%s'] * len(keys))
    query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

    with conn.cursor() as cur:
        for row in data:
            cur.execute(query, tuple(row.values()))
    conn.commit()

def insert_all(conn, normalized_data):
    print("📥 Inserting brands")
    insert_data(conn, "brands", normalized_data["brands"])

    print("📥 Inserting computers")
    insert_data(conn, "computers", normalized_data["computers"])

    print("📥 Inserting cpus")
    insert_data(conn, "cpus", normalized_data["cpus"])

    print("📥 Inserting memory_modules")
    insert_data(conn, "memory_modules", normalized_data["memory_modules"])

    print("📥 Inserting storage_devices")
    insert_data(conn, "storage_devices", normalized_data["storage_devices"])

    print("📥 Inserting gpus")
    insert_data(conn, "gpus", normalized_data["gpus"])
