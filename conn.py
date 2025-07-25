import psycopg2
from psycopg2 import OperationalError
import streamlit as st
import os

def get_connection():
    try:
        conn = psycopg2.connect(
            user=os.environ["POOLER_USER"],
            password=os.environ["POOLER_PASSWORD"],
            host=os.environ["POOLER_HOST"],
            port=os.environ["POOLER_PORT"],
            dbname=os.environ["POOLER_DATABASE"]
        )
        # st.success("✅ Connected successfully.")
        return conn

    except OperationalError as e:
        st.error("❌ Failed to connect.")
        st.exception(e)
        return None

# def get_connection():
#     try:
#         conn = psycopg2.connect(
#             user=st.secrets["POOLER_USER"],
#             password=st.secrets["POOLER_PASSWORD"],
#             host=st.secrets["POOLER_HOST"],
#             port=st.secrets["POOLER_PORT"],
#             dbname=st.secrets["POOLER_DATABASE"]
#         )
#         # st.success("✅ Connected successfully.")
#         return conn

#     except OperationalError as e:
#         st.error("❌ Failed to connect.")
#         st.exception(e)
#         return None
