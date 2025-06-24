import mysql.connector

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="admin",
        password="admin123",
        database="test_db"
    )
