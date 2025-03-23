🚀 Docker Bridge: Balancing Isolation & Connectivity
📌 Objective
The goal of this exercise is to explore and demonstrate network isolation in Docker containers. We will examine how containers within the same custom bridge network can communicate, while those on different networks remain isolated. Understanding this is crucial for securing microservices and containerized applications.

🌐 Introduction to Docker Networking
Docker networking is fundamental for containerized applications, allowing containers to communicate while ensuring security and isolation. Docker provides several networking options:

🔹 Types of Docker Networks:
Bridge Network (Default) – Allows communication between containers using internal IPs unless restricted.
Custom Bridge Network – Offers better control and supports name-based resolution.
Host Network – Attaches containers directly to the host’s network stack.
Overlay Network – Enables communication across multiple hosts (Docker Swarm).
Macvlan Network – Assigns a MAC address to each container, making them appear as separate devices.
None Network – Completely disables networking.
For this demonstration, we focus on the custom bridge network, which improves control and network isolation.

⚡ Why Use a Custom Bridge Network?
A custom bridge network offers several advantages: ✅ Improved Security – Containers on different networks are isolated by default. ✅ Better Performance – Direct communication without host networking stack overhead. ✅ DNS-Based Resolution – Containers communicate via names instead of IPs. ✅ Greater Control – Define specific subnets, IP ranges, and gateways.

To demonstrate, we create a custom bridge network called Rakshan-bridge and connect multiple containers.

🔧 1. Creating a Custom Bridge Network
docker network create --driver bridge --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 Rakshan-bridge
🔍 Explanation:
--driver bridge → Uses the default bridge network mode.
--subnet 172.20.0.0/16 → Defines the network’s IP range.
--ip-range 172.20.240.0/20 → Allocates IPs dynamically.
🚀 2. Running Containers in the Custom Network
Running Redis Container (Rakshan-database)
docker run -itd --net=Rakshan-bridge --name=Rakshan-database redis
Running BusyBox Container (Rakshan-server-A)
docker run -itd --net=tara-bridge --name=Rakshan-server-A busybox
📌 Check Container IPs
docker network inspect Rakshan-bridge
Expected Output:

 Rakshan-database: 172.20.240.1
 Rakshan-server-A: 172.20.240.2
🔄 3. Testing Communication Between Containers
Ping from Rakshan-database to Rakshan-server-A
docker exec -it Rakshan-database ping 172.20.240.2
Ping from Rakshan-server-A to Rakshan-database
docker exec -it Rakshan-server-A ping 172.20.240.1
✅ Expected Outcome: Both containers should successfully ping each other.

🚧 4. Demonstrating Network Isolation with a Third Container
We add another container (Rakshan-server-B) on the default bridge network.

docker run -itd --name=Rakshan-server-B busybox
📌 Get IP of Rakshan-server-B
docker inspect -format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' Rakshan-server-B
(Example IP: 172.17.0.2)

❌ 5. Testing Communication Between Different Networks
Ping from Rakshan-database to Rakshan-server-B:

docker exec -it Rakshan-database ping 172.17.0.2
🚨 Expected Outcome: The ping should fail, as they are on different networks.

🔍 6. Confirming Network Isolation
Inspect Networks
docker network inspect Rakshan-bridge
docker network inspect bridge
✅ Rakshan-bridge should contain Rakshan-database & Rakshan-server-A. ✅ bridge should contain Rakshan-server-B.

🏆 Conclusion
Containers in the same network can communicate.
Containers in different networks are isolated by default.
Docker’s networking model ensures security and separation unless explicitly connected.
🚀 Now you have mastered Docker Bridge Networking! 🎯