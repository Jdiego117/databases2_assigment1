import streamlit as st
import pandas as pd
from customer_repository import get_all_customers

st.title('Get database data')

customers = get_all_customers()

df = pd.DataFrame(customers, columns=['Id', 'Name', 'Email', 'Phone', 'Birthdate', 'movie_code', 'Movie title', 'Release date', 'Genres', 'Duration'])

st.write(df)

