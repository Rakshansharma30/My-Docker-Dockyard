import streamlit as st
import time

LOG_FILE = "/data/app.log"

st.set_page_config(page_title="Live Log Viewer", layout="wide")
st.title("📜 Live Log Viewer - Exp-3")

log_container = st.empty()

def read_logs():
    try:
        with open(LOG_FILE, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Log file not found."

while True:
    logs = read_logs()
    log_container.text(logs)
    time.sleep(2)
