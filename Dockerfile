FROM python:3.10-slim

WORKDIR /app

ARG GEMFURY_URL

ENV GEMFURY_URL=$GEMFURY_URL

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENV PYTHONPATH = $PYTHONPATH:/app/

CMD ["gunicorn", "main:server", "--timeout", "300"]
