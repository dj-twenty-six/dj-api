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
- http://localhost:8000/docs
```bash
$ uvicorn app.main:app --reload
```

### ref
- https://fastapi.tiangolo.com/ko/#_4