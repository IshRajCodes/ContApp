from flask import Flask
from datetime import datetime
import psycopg2
import os

app = Flask(__name__)

def check_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            host=os.getenv("DB_HOST"),
            port="5432"
        )
        conn.close()
        return "✅ Connected to the database!"
    except Exception as e:
        return f"❌ DB connection failed: {e}"

@app.route("/")
def home():
    status = check_db()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
    <head><meta http-equiv="refresh" content="30"></head>
    <body>
      <h2>{status}</h2>
      <p>Timestamp: {timestamp}</p>
      <p>Auto-refreshing every 30 seconds...</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)