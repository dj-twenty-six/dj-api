# dj-api

### preparation
- https://pdm.fming.dev/latest/#installation
```bash
$ source .venv/bin/activate
$ pdm add fastapi
$ pdm add "uvicorn[standard]"
$ pdm add -dG test pytest pytest-cov
```

### RUN SERVER
- http://localhost:8000
```bash
$ uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['/home/dj26/code/dj-api']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20346] using WatchFiles
INFO:     Started server process [20348]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:45600 - "GET /weather HTTP/1.1" 200 OK
```

### API
- http://localhost:8000/docs
```bash
$ curl -X 'GET' 'http://localhost:8000/weather' -H 'accept: application/json'
{"location":"동작구 신대방2동","weather_condition":"맑음","temperature":"18.4"}

$ curl http://localhost:8000/weather
{"location":"동작구 신대방2동","weather_condition":"맑음","temperature":"18.4"}
```

### Docker
- http://localhost:9040/docs
```bash
$ docker build -t dj-api:0.4.0 .
$ docker run -dit --name dj-api040 -p 9040:80 dj-api:0.4.0
```

### Deploy fly.io
```bash
$ flyctl launch

Visit your newly deployed app at https://dj-api.fly.dev/
```

### Reg Docker Hub
- https://hub.docker.com/r/pysatellite/dj-api/tags
```bash
$ docker build -t pysatellite/dj-api:0.6.0 .
$ docker push pysatellite/dj-api:0.6.0
```

### ref
- https://fastapi.tiangolo.com/ko/#_4
- https://fastapi.tiangolo.com/ko/deployment/docker/?h=docker