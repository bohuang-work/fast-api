# Fast API

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

RESTful-api implemented using Fast-API framework:

- Hexagon structure
- HTTP methods: CRUD
- PostgreSQL
- Pydantic Model

## code quality

- 100% type annotation
- linter: ruff
- static type checking: mypy
- code formatting: black

## dependecies management

### peotry

- fastapi = "0.101.1"
- pg8000 = "1.30.1"
- pydantic = "2.2.0"
- pydantic-settings = "2.0.3"
- python = "^3.11"
- requests = "2.31.0"
- sqlalchemy = "2.0.20"
- uvicorn = "0.23.2"

## pre installation

- Docker
- Python >= 3.11

## Deployments

#### docker compose

1. run docker compose to start API and postgresDB

```
   cd backend/
   docker docker-compose up
```

2. make sure 8080 is free, then open swagger:
   http://127.0.0.1:8080/docs

#### k3d

use k3d to create a single Node cluster locally for deployments.

1. install automation tool "task" and k3d:

```
   ./bootstrap.sh
   ./setup.sh
```

2. create k3d cluster:

```
   cd k8s/deployments/local
   task create-k3d
```

3. install postgres:

```
   task install-postgresql
```

4. update helm charts:

```
   task generate-charts
```

5. build and push migration and backend image to k3d local docker registry:

```
   task build-and-push-migrations
   task build-and-push-backend
```

6. deploy fastapi:

```
   task install-fastapi
```

7. port forward apis and visite swagger:

```
   kubectl port-forward  fastapi-backend-<pod id> 8080:8080
```

http://127.0.0.1:8080/docs

## swager

![alt text](https://github.com/bohuang-work/fast-api/blob/main/fastAPI.png)
