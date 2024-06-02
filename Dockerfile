FROM python:3.10.12-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirments.txt

COPY . .

CMD ["python3"]