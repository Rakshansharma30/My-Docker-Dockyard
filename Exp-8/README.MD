🚀 Deploying a Dockerized Application on AWS EC2
Easily deploy a Dockerized app on an AWS EC2 instance using this step-by-step guide!

📌 Prerequisites
Make sure you have the following ready:

✔️ AWS EC2 Instance (Amazon Linux 2)
✔️ SSH Key Pair (e.g., vs-kp-1.pem)
✔️ Docker Installed (or install during the steps)
✔️ Required files: Dockerfile, app.py, requirements.txt, mushrooms.csv

🛠 Deployment Steps
1️⃣ Update the System Packages
bash
Copy
Edit
sudo yum update -y
2️⃣ Install Docker
bash
Copy
Edit
sudo amazon-linux-extras install docker
3️⃣ Start the Docker Service
bash
Copy
Edit
sudo service docker start
4️⃣ Create a Directory for Application Files
bash
Copy
Edit
mkdir downloads
5️⃣ Transfer Files from Local to EC2
Make sure your SSH key permissions are correct:

bash
Copy
Edit
chmod 600 vs-kp-1.pem
Then transfer your files:

bash
Copy
Edit
scp -i vs-kp-1.pem Dockerfile app.py requirements.txt mushrooms.csv ec2-user@<EC2-Public-IP>:/home/ec2-user/downloads
Replace <EC2-Public-IP> with your instance’s public IP.

6️⃣ Build the Docker Image
Move to the correct directory if needed, then build:

bash
Copy
Edit
cd downloads
sudo docker build -t my_app:v1.0 -f Dockerfile .
7️⃣ Run the Docker Container
bash
Copy
Edit
sudo docker run -d -p 8501:8501 my_app:v1.0
The application will now be accessible publicly on port 8501.

🎯 Result
✅ Your Dockerized application is now live on the EC2 instance!

🔗 Access it via:

bash
Copy
Edit
http://<EC2-Public-IP>:8501
🔍 Useful Docker Commands
📋 Check running containers:

bash
Copy
Edit
sudo docker ps
📜 View container logs:

bash
Copy
Edit
sudo docker logs <container-id>
🛑 Stop a running container:

bash
Copy
Edit
sudo docker stop <container-id>