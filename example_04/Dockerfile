FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir Flask python-dotenv

CMD ["python", "app.py"]