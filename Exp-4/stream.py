import streamlit as st
import psycopg2
st.markdown("""
    <style>
        .title {
            color: #333;
            font-size: 36px;
            font-weight: bold;
        }
        .subtitle {
            color: #555;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .card {
            background-color: #ffffff;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .data {
            font-size: 18px;
            line-height: 1.6;
            color: #444;
        }
        .data span {
            color: #0073e6;
        }
        .error {
            color: #e74c3c;
        }
        .success {
            color: #2ecc71;
        }
        .warning {
            color: #f39c12;
        }
    </style>
""", unsafe_allow_html=True)
# Establishing connection to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydb",
        user="admin",
        password="adminpassword",
        host="my_postgres",  # Container name of the PostgreSQL service
        port="5432"
    )
    return conn


# Streamlit app title
st.title("Streamlit App with PostgreSQL")

try:
    # Connect to the database
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch data from the 'users' table
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()

    # Display data
    st.write("### User Data from PostgreSQL")
    for row in rows:
        st.write(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    # Close the cursor and connection
    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Error connecting to the database: {e}")
