🐳 Dockerized Streamlit Development Environment
This project demonstrates how to containerize a Streamlit application using Docker. The environment ensures consistency across different systems and simplifies the deployment process.

📂 Directory Structure
bash
Copy
Edit
project_root/
│── .streamlit/              # Configuration for Streamlit UI
│   └── config.toml
│── src/
│   └── main.py              # Main Streamlit application logic
│── Dockerfile               # Docker image definition
│── requirements.txt         # List of Python dependencies
│── README.md                # Project documentation
🚀 Prerequisites
Ensure the following dependencies are installed on your system:

Docker 🐳 (Check with docker --version)

Python 3.9+ 🐍 (Check with python --version)

pip 📦 (Check with pip --version)

⚡️ Steps to Run the Project
Clone the Repository

bash
Copy
Edit
git clone https://github.com/YourGitHubUsername/My-Docker-Dockyard.git
cd My-Docker-Dockyard/Dockerized Streamlit Development Environment
Build the Docker Image

bash
Copy
Edit
docker build -t streamlit-app .
Run the Docker Container

bash
Copy
Edit
docker run -p 8501:8501 streamlit-app
Access the Application Open your browser and go to:

arduino
Copy
Edit
http://localhost:8501
📜 File Descriptions
1️⃣ .streamlit/config.toml
Contains Streamlit configurations for the local environment.

toml
Copy
Edit
[server]
headless = true
runOnSave = true
fileWatcherType = "poll"
2️⃣ src/main.py
Main Streamlit application file that includes:

🏠 Home Page: Introduction to the application.

📊 Data Explorer: Upload CSV files and analyze data.

📈 Visualization: Generate dynamic charts and graphs.

3️⃣ Dockerfile
Defines the Docker container environment.

Dockerfile
Copy
Edit
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8501
CMD ["streamlit", "run", "src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
4️⃣ requirements.txt
Contains the required Python dependencies.

nginx
Copy
Edit
streamlit
pandas
numpy
matplotlib
plotly
🎨 Application Features
✅ Home Page: Introduction and instructions.
✅ Data Explorer: CSV file upload, preview, and analysis.
✅ Visualization: Line charts, bar charts, and scatter plots using Plotly.

🐞 Troubleshooting
Port Already in Use Error

Stop any existing services using port 8501:

bash
Copy
Edit
docker stop $(docker ps -q --filter "expose=8501")
Permission Denied Error (Linux/Mac)

Run Docker with sudo:

bash
Copy
Edit
sudo docker build -t streamlit-app .
File Not Found Error

Ensure that all necessary files (like requirements.txt) are correctly named and placed in the project root.