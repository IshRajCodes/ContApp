from flask import Flask
import psycopg2

app = Flask(__name__)

def check_db():
    try:
        conn = psycopg2.connect(
            dbname="appdb",
            user="user",
            password="pass",
            host="db",
            port="5432"
        )
        conn.close()
        return "✅ Connected to the database!"
    except Exception as e:
        return f"❌ DB connection failed: {e}"

@app.route("/")
def home():
    return f"""
    <html>
    <head><meta http-equiv="refresh" content="30"></head>
    <body>
      <h2>{check_db()}</h2>
      <p>Auto-refreshing every 30 seconds...</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
