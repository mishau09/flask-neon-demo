from flask import Flask, request
import psycopg
import os
from dotenv import load_dotenv

DATABASE_URL = os.getenv("DATABASE_URL")
load_dotenv()

app = Flask(__name__)

@app.route("/",methods-["GET","POST"])
def home():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(""
                        CREATE TABLE IF NOT EXISTS notes(
                            id SERIAL PRIMARY KEY, content TEXT)""))
                        