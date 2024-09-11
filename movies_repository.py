import os
import mysql.connector
from mysql.connector import Error

def bulk_insert_movies(df_movies, table_name='movies'):
    connection = None
    cursor = None
    
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            query = f"""
            INSERT INTO {table_name} (movie_code, title, release_date, duration, genres)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            movies_data = df_movies.to_records(index=False).tolist()
            
            cursor.executemany(query, movies_data)
            
            connection.commit()
            
            print(f"{cursor.rowcount} rows inserted successfully.")
        
    except Error as e:
        print(f"The error '{e}' occurred")
        if connection:
            connection.rollback()
    finally:
        if cursor is not None:
            cursor.close()
            
        if connection is not None and connection.is_connected():
            connection.close()