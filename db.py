import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="onboarding_db",
        user="postgres",
        password="postgres",
        port="5432"
    )
    cursor = conn.cursor()
except Exception as e:
    print("Database connection warning (Offline mode active):", e)
    conn = None
    cursor = None
