# DevOps Assessment — Flask App (Local)

This repository contains a simple Flask app instrumented with Prometheus metrics and a full local-first DevOps setup: Docker, docker-compose, Jenkins pipeline, Prometheus & Grafana, Kubernetes manifests for Minikube, and a CI workflow.

## What is included
- `app.py` — Flask app (you provided; unchanged).
- `Dockerfile` — builds the app.
- `Jenkinsfile` — declarative pipeline to build, test, build Docker image and run container (for local Jenkins).
- `docker-compose.yml` — brings up app, Jenkins, Redis, Nginx, Prometheus, Grafana.
- `prometheus_config/prometheus.yml` — Prometheus scrape config.
- `nginx/default.conf` — proxy to app.
- `flask-deployment.yaml`, `flask-service.yaml` — Kubernetes manifests for Minikube.
- `.github/workflows/ci.yml` — basic GitHub Actions workflow (build & test).
- `requirements.txt` — Python deps.
- `test_app.py` — simple pytest tests (exists in repo).

## Quick local run (Docker Compose)
1. Build & start everything:
   ```bash
   docker-compose up --build -d

