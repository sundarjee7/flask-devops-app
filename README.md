# Flask DevOps Assessment Project

## **Project Overview**
This project demonstrates a local DevOps setup including CI/CD, Docker, and Kubernetes deployment for a sample Flask application.  
The project was designed to satisfy the following objectives:  

- Set up a local CI/CD pipeline with Jenkins and Docker.  
- Dockerize a Flask app and run it locally.  
- Deploy the Dockerized app to a local Kubernetes cluster (Minikube).  
- Use Prometheus for monitoring application metrics.  
- Automate environment setup using shell scripts and Docker Compose.  

---

## **Assessment Tasks Completed**
1. **CI/CD Pipeline with Jenkins + Docker**  
   - Jenkins pipeline configured using `Jenkinsfile`.  
   - Application build, test, and Docker image creation implemented.  
   - Docker container runs on successful build.  

2. **Kubernetes Deployment with Minikube**  
   - Dockerized Flask app deployed to Minikube.  
   - Kubernetes manifests (`flask-deployment.yaml` and `flask-service.yaml`) included.  
   - Verified pods and services using `kubectl`.  

3. **Infrastructure Automation with Shell + Docker Compose**  
   - Shell scripts (`config.sh`, `run-helper.sh.template`) automate setup.  
   - Docker Compose (`docker-compose.yml`) brings up app and services.  

4. **Monitoring Stack with Prometheus**  
   - Flask app exposes `/metrics` endpoint for Prometheus.  
   - Prometheus config files included under `prometheus_config/`.  
   - Metrics can be visualized in Grafana (via Docker Compose).  

5. **Optional / Bonus Tasks**  
   - Local GitHub Actions runner prepared (not pushed due to large files).  
   - All optional configurations for monitoring and automation included.  

---

## **Setup Instructions**

### **1. Prerequisites**
- Docker: [Install Docker](https://docs.docker.com/get-docker/)  
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)  
- Python 3.x: [Install Python](https://www.python.org/downloads/)  
- kubectl: [Install kubectl](https://kubernetes.io/docs/tasks/tools/)  
- Minikube: [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)  

---

### **2. Clone the Repository**
```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

