# Fast API

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

## setup

1. run docker compose to start API and postgresDB

```
   cd backend
   docker docker-compose up
```

2. make sure 8080 is free, then open swagger:
   http://127.0.0.1:8080/docs

## swager

![alt text](https://github.com/bohuang-work/fast-api/blob/main/fastAPI.png)
