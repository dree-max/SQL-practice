import time
from db_utils import get_conn
import random

def execute_query(cursor, query):
    start = time.time()
    cursor.execute(query)
    end = time.time()
    return end - start

def main():
    conn = get_conn()
    cur = conn.cursor()

    # 1. Drop and create table (split into two execute calls)
    cur.execute("DROP TABLE IF EXISTS users;")
    cur.execute("""
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        age INT
    );
    """)

    # 2. Insert data (example for 1000 users)
    print("Inserting rows...")
    start = time.time()
    for i in range(1, 1001):
        cur.execute(
            "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)",
            (f"User {i}", f"user{i}@mail.com", int(100 * random.random()))
        )
    conn.commit()
    print(f"Inserted in {time.time() - start:.2f} seconds")

    # 3. Add nullable column
    print("Adding nullable column...")
    t1 = execute_query(cur, "ALTER TABLE users ADD COLUMN phone_number VARCHAR(10);")
    conn.commit()
    print(f"Nullable column added in {t1:.2f} seconds")

    # 4. Drop column
    cur.execute("ALTER TABLE users DROP COLUMN phone_number;")
    conn.commit()
    # 5. Add NOT NULL column with default
    print("Adding NOT NULL column with default...")
    t2 = execute_query(cur, "ALTER TABLE users ADD COLUMN phone_number VARCHAR(10) NOT NULL DEFAULT '0000000000';")
    conn.commit()
    print(f"Non-nullable column without default added in {t2:.2f} seconds")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
