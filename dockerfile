FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11.2

COPY ./app /app

RUN pip install sqlalchemy

EXPOSE 80