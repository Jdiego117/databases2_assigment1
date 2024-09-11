import streamlit as st
import pandas as pd
from movies_repository import bulk_insert_movies
from customer_repository import bulk_insert_customers

st.title('Import data from Excel')

def extract_db_from_excel(movies_excel_file, customers_excel_file):
    try: 
        movies_df = pd.read_excel(movies_excel_file)
        customers_df = pd.read_excel(customers_excel_file)
    except Exception as e:
        st.write(f'Error reading the excel file: {e}')
        return None
    
    movies_df = movies_df.rename(columns={
        'MovieCode' : 'movie_code',
        'Movie title' : 'title',
        'Release Date' : 'release_date',
        'Duration' : 'duration',
        'Movie Genres' : 'genres'
    })
    
    movies_df['duration'] = movies_df['duration'].astype(int)
    movies_df['release_date'] = movies_df['release_date'].dt.strftime('%Y-%m-%d')
    
    customers_df = customers_df.rename(columns={
        'Name' : 'name',
        'Email' : 'email',
        'Phone' : 'phone',
        'Birthdate' : 'birthdate',
        'MovieCode' : 'movie_code'
    })
    
    customers_df['phone'] = customers_df['phone'].astype(str)
    customers_df['birthdate'] = customers_df['birthdate'].dt.strftime('%Y-%m-%d')
    
    bulk_insert_movies(movies_df)
    bulk_insert_customers(customers_df)
    
    final_df = pd.merge(customers_df, movies_df, on='movie_code', how='inner')
    
    st.write(final_df)
    
movies_excel = st.file_uploader('Upload the movies excel file', type=['xlsx', 'xls'])
customers_excel = st.file_uploader('Upload the customers excel file', type=['xlsx', 'xls'])

if st.button('Upload'):
    if movies_excel is not None and customers_excel is not None:
        extract_db_from_excel(movies_excel, customers_excel)