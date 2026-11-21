import psycopg2
import getpass
import os
def get_connection():
    try:
        connection=psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "incident_db"),
            user=os.getenv("DB_USER", getpass.getuser()),
            password=os.getenv("DB_PASSWORD") or None
        )
        return connection
    except psycopg2.Error as e:
        print("Error connecting to the databsase:", e)
        return None
    
def get_all_incidents():
    connection=get_connection()
    if connection is None:
        return []
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                           SELECT id, description, predicted_category,similarity_score,created_at
                           FROM incidents
                           ORDER BY similarity_score DESC
                           """)
            incidents=cursor.fetchall()
            return incidents
    except psycopg2.Error as e:
        print("Error connecting to the databsase:", e)
        return None
    finally:
        connection.close()


    


