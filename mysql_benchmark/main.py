import time
import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="db_mysql",
        port=3306,
        user="user",
        password="password",
        database="testdb"
    )

def execute_query(cursor, query):
    start = time.time()
    cursor.execute(query)
    return time.time() - start

def main():
    conn = get_conn()
    cur = conn.cursor()

    print("Creating table...")
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        age INT
    );
    """)
    conn.commit()
    total=10000000
    batch_size=10000
    print(f"Inserting {total:,} users in batches of {batch_size:,}...")
    from time import time
    start = time()
    
    
    for start_id in range(1, total + 1, batch_size):
        end_id = min(start_id + batch_size, total + 1)
        batch = [(
            f"User {i}",
            f"user{i}@mail.com",
            i % 100
        ) for i in range(start_id, end_id)]

        cur.executemany("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", batch)
        conn.commit()
        print(f"Inserted {end_id - 1:,} rows...", end="\r")

    print(f"\n✅ Done inserting {total:,} rows in {time() - start:.2f} seconds.")

    print("Adding nullable column...")
    t1 = execute_query(cur, "ALTER TABLE users ADD COLUMN phone_number VARCHAR(10);")
    print(f"Nullable column added in {t1:.2f} seconds")

    print("Dropping column...")
    cur.execute("ALTER TABLE users DROP COLUMN phone_number;")
    conn.commit()

    print("Adding NOT NULL column with default...")
    t2 = execute_query(cur, "ALTER TABLE users ADD COLUMN phone_number VARCHAR(10) NOT NULL DEFAULT '0000000000';")
    print(f"Non-nullable column added in {t2:.2f} seconds")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
