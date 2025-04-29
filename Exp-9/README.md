☸️ Minikube with Docker on Windows
🚀 Run Kubernetes Locally with Minikube & Docker 🐳
🌟 Introduction
Minikube is a lightweight tool that lets you run a Kubernetes cluster locally.
Perfect for developers who want to test Kubernetes without needing cloud infrastructure.
Minikube supports various drivers like Docker, VirtualBox, and Hyper-V, making Kubernetes development easy and accessible.

🛠️ Prerequisites
Before getting started, make sure you have the following installed:

✅ 1. Install Docker Desktop 🐋
Download Docker Desktop

Enable WSL 2 backend (recommended) ⚙️

If you are using Windows Pro/Enterprise, also enable Hyper-V 🔧

Ensure Docker Desktop is running before using Minikube.

✅ 2. Install Minikube 📦
Install via Chocolatey (in CMD or PowerShell as Admin):

bash
Copy
Edit
choco install minikube
No Chocolatey? Install Minikube manually.

✅ 3. Install kubectl (Kubernetes CLI) 🔗
Install via Chocolatey:

bash
Copy
Edit
choco install kubernetes-cli
Verify the installation:

bash
Copy
Edit
kubectl version --client
🚀 Getting Started: Minikube with Docker
✅ Step 1: Start Minikube 🏁
Make sure Docker is running. Then, start Minikube using Docker as the driver:

bash
Copy
Edit
minikube start --driver=docker
Check the cluster status:

bash
Copy
Edit
minikube status
🏗️ Deploying Your First Application
✅ Step 2: Deploy Nginx Web Server 🌐
1️⃣ Create a Deployment
bash
Copy
Edit
kubectl create deployment nginx --image=nginx
2️⃣ Expose the Deployment
bash
Copy
Edit
kubectl expose deployment nginx --type=NodePort --port=80
3️⃣ Access the Service
bash
Copy
Edit
minikube service nginx --url
Open the provided URL in your browser to see Nginx running! 🎉

⚙️ Managing the Kubernetes Cluster
✅ Check Running Pods 📋
bash
Copy
Edit
kubectl get pods
✅ Scale the Deployment 📈
Increase replicas to 3:

bash
Copy
Edit
kubectl scale deployment nginx --replicas=3
Check updated pods:

bash
Copy
Edit
kubectl get pods
✅ Delete Deployment and Service 🗑️
bash
Copy
Edit
kubectl delete service nginx
kubectl delete deployment nginx
❌ Stopping and Cleaning Up Minikube
✅ Stop Minikube 🔻
bash
Copy
Edit
minikube stop
✅ Delete the Cluster 🗑️
bash
Copy
Edit
minikube delete
This removes the entire local Kubernetes environment.

🎯 Conclusion
Running Kubernetes locally with Minikube + Docker is fast, lightweight, and doesn't require setting up extra VMs.
It’s perfect for learning, testing, and building applications on Kubernetes without complex cloud setups.

