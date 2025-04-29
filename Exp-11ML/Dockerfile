# Use a slim Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and source code
COPY requirements.txt requirements.txt
COPY main.py main.py
COPY titanic_model.pkl titanic_model.pkl

# Install dependencies
RUN pip install -r requirements.txt

# Expose the Streamlit port
EXPOSE 8511

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8511", "--server.address=0.0.0.0"]