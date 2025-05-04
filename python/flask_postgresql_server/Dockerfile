FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY migrations ./migrations
COPY entrypoint.sh .

EXPOSE 8080

ENV FLASK_APP=app:create_app
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["./entrypoint.sh"]
