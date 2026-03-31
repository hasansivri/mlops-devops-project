# 🚀 MLOps DevOps Project - Production Ready

## Stack
- MLflow (with PostgreSQL + MinIO)
- Docker / Docker Compose
- Kubernetes
- GitLab CI/CD
- FastAPI for model serving

## Run Locally

1. Start MLflow stack:
```bash
docker-compose up -d

2. Start model API:
cd model-api
docker build -t model-api .
docker run -e MLFLOW_TRACKING_URI=http://mlflow:5000 -p 8000:8000 model-api

##      CI/CD Flow
Commit to GitLab triggers pipeline
Docker image build & push
Kubernetes deployment

## Production Notes
Create Kubernetes secret for Docker Hub: kubectl create secret docker-registry dockerhub-secret ...
Ensure MinIO bucket mlflow-artifacts exists
Set MLFLOW_TRACKING_URI in environment variables


mlops-devops-project/
│
├── mlflow/
│   ├── docker-compose.yml
│
├── model-api/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
└── README.md