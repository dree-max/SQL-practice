import time
from db_utils import get_conn

def execute_query(cursor, query):
    start = time.time()
    cursor.execute(query)
    end = time.time()
    return end - start

def main():
    conn = get_conn()
    conn.autocommit = True
    cur = conn.cursor()

    # 1. Create table
    cur.execute("""
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT,
        age INT
    );
    """)


    start = time.time()
    # 2. Insert data
    print("Inserting rows...")
    cur.execute("""
    INSERT INTO users (name, email, age)
    SELECT
        'User ' || g,
        'user' || g || '@mail.com',
        floor(random() * 100)::int
    FROM generate_series(1, 10000000) AS g;
    """)

    
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
    #t2 = execute_query(cur, "ALTER TABLE users ADD COLUMN phone_number VARCHAR(10) NOT NULL;")
    conn.commit()
    print(f"Non-nullable column without default added in {t2:.2f} seconds")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
