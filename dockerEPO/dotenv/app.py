from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"Database version: {db_version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

