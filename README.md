# SQL-practice

A Python-based benchmarking project for experimenting with SQL table operations and performance, using MySQL as the backend. The project supports running MySQL in Docker and is compatible with MySQL Workbench for database inspection.

---
Inspired by a question from https://x.com/asmah2107 on a tweet https://x.com/asmah2107/status/1937224695625187744

Quick question :

You need to add a new, required phone_number column to your users table, which has 500 million rows.

You write a simple ALTER TABLE script.

You run it during a "maintenance window."

It locks the entire users table for 8 hours while it adds the new column to every row.

For 8 hours, no one can sign up or log in.

Pain right ? You cannot perform "stop the world" operations on a live, large scale database

How will you do a “Painless Database Migration” ?

## Features

- **Benchmarking Table Operations:**  
  - Create, drop, and alter tables.
  - Insert large numbers of rows.
  - Measure and print timing for each operation.

- **MySQL in Docker:**  
  - Easily spin up a MySQL server using Docker Compose.
  - Data persists across container restarts.

- **MySQL Workbench Compatible:**  
  - Inspect and manage your database visually.

---

## Prerequisites

- **Python 3.8+**
- **Docker & Docker Compose**
- **MySQL Workbench** (optional, for GUI inspection)

---

## Setup

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd SQL-practice
```

### 2. Install Python Dependencies

```sh
pip install -r benchmark/requirements.txt
```

### 3. Start MySQL with Docker

```sh
docker-compose up -d
```

- This will start a MySQL 8.0 server on port **3307** (host) mapped to **3306** (container).
- Credentials:
  - **Host:** `localhost`
  - **Port:** `3307`
  - **User:** `admin`
  - **Password:** `admin123`
  - **Database:** `test_db`

### 4. (Optional) Connect with MySQL Workbench

- Create a new connection:
  - Host: `localhost`
  - Port: `3307`
  - User: `admin`
  - Password: `admin123`
- Select the `test_db` schema to view tables created by the script.

---

## Running the Benchmark

Run the main benchmarking script:

```sh
python benchmark/main.py
```

This will:
- Drop and recreate the `users` table.
- Insert 1,000 users (can be adjusted in the script).
- Add and drop columns, measuring the time for each operation.

All output will be printed to the terminal.

---

## Project Structure

```
SQL-practice/
  benchmark/
    db_utils.py         # Database connection utility
    main.py             # Main benchmarking script
    requirements.txt    # Python dependencies
  db/
    init.sql            # (Unused, for custom SQL if needed)
  docker-compose.yml    # Docker Compose config for MySQL
  README.md             # Project documentation
```

---

## Troubleshooting

- **Can't connect to MySQL:**  
  - Ensure Docker is running and the container is started (`docker ps`).
  - Make sure you are using port `3307` in your script and Workbench.
  - Wait a minute after starting the container for MySQL to initialize.

- **Table not visible in Workbench:**  
  - Make sure you are connected to the Docker MySQL instance (port `3307`).
  - Refresh the schema list in Workbench.

- **Port conflicts:**  
  - If port `3307` is in use, change the port mapping in `docker-compose.yml` and your code.

---

## Customization

- **Change number of inserted users:**  
  Edit the loop in `benchmark/main.py`:
  ```python
  for i in range(1, 1001):  # Change 1001 to desired number + 1
      ...
  ```

- **Add more benchmarks:**  
  Add new SQL operations in `main.py` as needed.

---
**froked from 

## License

MIT License

To Only run the mysql part:
docker-compose up --build app_mysql