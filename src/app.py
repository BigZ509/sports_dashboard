import  os
from dotenv import load_dotenv
import psycopg2
from flask import Flask


load_dotenv()
# Load database connection parameters from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")  
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)
cur = conn.cursor()
cur.execute("SELECT version();")
db_version = cur.fetchone()
print(f"Connected to database. PostgreSQL version: {db_version}")


headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": RAPIDAPI_HOST
}



app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Sports Dashboard!"

# Example of a method called from app.py
def greet_user(name):
    return f"Welcome, {name}!"

@app.route('/welcome')
def welcome():
    return greet_user("Big Z")

if __name__ == '__main__':
    app.run(debug=True)
