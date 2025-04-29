# Use a base Python image
FROM python:3-slim

WORKDIR /app

COPY app.py /app/
COPY viewer.py /app/

RUN pip install streamlit

RUN mkdir -p /data

CMD ["sh", "-c", "python app.py & streamlit run viewer.py --server.port=8503 --server.address=0.0.0.0"]
