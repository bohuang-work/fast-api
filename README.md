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
   cd backend/
   poetry install
```

4. run postgeSQL using docker compose:

```
   open a new terminal
   cd fast-api/docker/
   docker-compose up
```

5. run backend service:

```
   back to the venv terminal
   cd /fast-api/backend/src
   ./cmd/run.sh
```

6. open:
   http://127.0.0.1:8080/docs

## swager

![alt text](https://github.com/bohuang-work/fast-api/blob/main/fastAPI.png)
