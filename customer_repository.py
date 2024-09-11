import os
import mysql.connector
from mysql.connector import Error

def bulk_insert_customers(df_customer, table_name='customers'):
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
            INSERT INTO {table_name} (name, email, phone, birthdate, movie_code)
            VALUES (%s, %s, %s, %s, %s)
            """

            customers_data = df_customer.to_records(index=False).tolist()
            
            cursor.executemany(query, customers_data)
            
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
    
def get_all_customers():
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
            
            query = """
            SELECT c.id, c.name, c.email, c.phone, c.birthdate, c.movie_code, movies.title, movies.release_date, movies.genres, movies.duration 
            FROM customers as c INNER JOIN movies ON c.movie_code = movies.movie_code;
            """
            
            cursor.execute(query)
            customers = cursor.fetchall()
            
    except Error as e:
        print(f"Error while getting courses from database: {e}")
    finally:
        cursor.close()
        connection.close()
        return customers