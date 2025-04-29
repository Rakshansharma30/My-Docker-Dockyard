FROM python:3-slim

RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir streamlit psycopg2-binary

EXPOSE 8504

CMD ["streamlit", "run", "stream.py", "--server.port=8504", "--server.address=0.0.0.0"]
