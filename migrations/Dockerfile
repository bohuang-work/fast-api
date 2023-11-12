# syntax=docker/dockerfile:1.3
FROM python:3.11-slim

# The enviroment variable ensures that the python output is set straight to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# init workspace
WORKDIR /app

# install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
# start server
ENTRYPOINT ["/app/run.sh"]