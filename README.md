# Next Fibonacci

FastAPI project that returns the next Fibonacci sequence number given a valid Fibonacci number as input.

## Description

This is a FastAPI python project with Uvicorn application server. It's packaged in a Docker container and hosted with docker-compose with a reverse proxy configuration using Nginx.

## Quickstart

To run locally for development, pip install the requirements.txt:

```
pip install --no-cache-dir --upgrade -r requirements.txt
```

Run with:

```
uvicorn app.main:app --reload
```

Access the running instance with http://localhost:8000/next-fibonacci?number=1

To run with docker-compose:
```
docker compose up -d
```

Access the running instance with http://localhost/next-fibonacci?number=1

## Reverse Proxy
The Nginx container exposes port 80 and passes to port 8000. It does so through the nginx.conf file which is bind mounted into the container.

The nginx.conf file is able to reference the uvicorn service with some Docker dns magic.

```
# nginx.conf
server {
  listen 80;

  location / {
    proxy_pass http://uvicorn:8000/;
  }
}
```
