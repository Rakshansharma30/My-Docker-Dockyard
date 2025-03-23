#!/bin/bash

# Exit on error
set -e

echo "🚀 Starting Docker Experiments Automation..."

# Define all experiment directories
EXPERIMENTS=(
    "Bakery Foundation Example on Windows"
    "Containerized MySQL, Agile & Efficient"
    "Docker Bridge, Balancing Isolation"
    "Docker Volume Persistence"
    "Dockerized Streamlit Development Environment"
    "Evidently AI Sets Sail in Docker"
    "Microservices Architecture using Docker Swarm"
    "Microservices Orchestration with Minikube"
    "Minikube with Docker on Windows"
    "Running a Streamlit App in Docker on AWS EC2"
    "Streamlit & PostgreSQL, docked"
    "Titanic Survival Predictor"
)

# Run all Docker Experiments
for EXPERIMENT in "${EXPERIMENTS[@]}"; do
    echo "⚙️ Running $EXPERIMENT..."
    cd "$EXPERIMENT"
    
    # Check if Dockerfile exists and build/run
    if [ -f Dockerfile ]; then
        docker build -t "${EXPERIMENT,,}" .
        docker run -d --name "${EXPERIMENT,,}_container" "${EXPERIMENT,,}"
    fi

    # Check if Docker Compose exists and run
    if [ -f docker-compose.yml ]; then
        docker-compose up -d
    fi

    # Apply Kubernetes Configurations
    if [ -f k8s_deployment.yaml ]; then
        kubectl apply -f k8s_deployment.yaml
    fi

    cd ..
done

echo "✅ All experiments executed successfully!"
