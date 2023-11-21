FROM python:3.11-slim

# RUN apt-get update && apt-get install -y postgresql

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENV PYTHONPATH=/app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3001"]
