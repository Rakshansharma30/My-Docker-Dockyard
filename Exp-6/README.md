🚀 Docker Network Experiment (Customized for Windows 11 + Docker Desktop)
This repository demonstrates how to create and test a custom Docker network (net-bridge) with multiple containers for seamless inter-container communication.
The experiment showcases how containers can communicate inside a user-defined bridge network on Docker Desktop (Windows 11).

🛠 Experiment Overview
Docker provides powerful networking capabilities, allowing containers to communicate securely.
In this experiment, we perform:

Creating a custom bridge network for isolated communication.

Running multiple containers attached to the custom network.

Inspecting and verifying container connectivity.

Testing inter-container communication using ping and container name resolution.

🔧 Experiment Setup (Environment)

Configuration	Details
OS	Windows 11 Home Single Language
Docker Version	Docker Desktop
Networking Driver	Bridge
Custom Network Name	net-bridge
1️⃣ Create a Custom Docker Network
bash
Copy
Edit
docker network create --driver bridge --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 net-bridge
2️⃣ Run Containers and Attach to the Network
🗄 Run Redis Database Container
bash
Copy
Edit
docker run -itd --net=net-bridge --name=cont_database redis
🖥 Run BusyBox Server Container
bash
Copy
Edit
docker run -dit --name=server-A --network=net-bridge busybox
3️⃣ Inspect Network and Containers
🔍 Inspect Network Details
bash
Copy
Edit
docker network inspect net-bridge
🔎 Inspect Specific Container Details
bash
Copy
Edit
docker inspect cont_database
🌐 Retrieve Container IP Address
bash
Copy
Edit
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cont_database
4️⃣ Testing Connectivity
🖥 Access Server Container Shell
bash
Copy
Edit
docker exec -it server-A sh
🔗 Test Ping by IP Address
bash
Copy
Edit
ping <Container-IP-of-cont_database>
(Replace <Container-IP-of-cont_database> with the IP fetched using inspect)

🔗 Test Ping by Container Name
bash
Copy
Edit
ping cont_database
📌 Observations
✅ Custom Bridge Network successfully allowed container-to-container communication.

✅ Ping by IP worked properly.

✅ Ping by Name may not work directly in BusyBox (due to minimal DNS setup).

✅ Docker Inspect is useful for verifying networking configurations and container IPs.

🏁 Conclusion
This experiment highlights Docker's networking strengths, especially in user-defined networks.
Understanding how containers communicate helps in building scalable microservices and cloud-native applications.

Custom Docker networks provide isolation, flexibility, and a production-like environment even during local development.

📸 Docker Network Connectivity Test
Here’s a screenshot from the experiment:



✅ The screenshot shows successful communication between containers over the net-bridge network.

📢 Author
👤 Rakshan Sharma

✅ Done!