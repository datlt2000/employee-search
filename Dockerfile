# fastapi-backend/Dockerfile
FROM python:3.10

WORKDIR /app/src
COPY requirements.txt .
COPY ./src .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
