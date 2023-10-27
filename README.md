# Fast API

RESTful-api implemented using Fast-API framework:

- hexagon structure
- HTTP methods: CRUD
- PostgreSQL

## pre installation

- Docker
- Python >= 3.8

## setup

1. create a python virtual environment and activate it:

```
   python3 -m venv venv
   source venv/bin/activate
```

2. install poetry

```
   python3 -m pip install poetry
```

3. install all dependencies using poetry:

```
   cd /fast-api/backend
   poetry install
```

4. run postgeSQL using docker compose:

```
   cd /docker
   docker-compose up
```

5. run backend service:

```
   cd /fast-api/backend/src
   ./cmd/run.sh
```

## swager

![alt text](https://github.com/bohuang-work/fast-api/blob/main/fastAPI.png)
