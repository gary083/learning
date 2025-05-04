FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./

EXPOSE 8080

ENV FLASK_APP=server:app
ENV DB_DIRECTORY=/usr/src/app/database

CMD ["gunicorn", "--workers", "1", "--bind", "0.0.0.0:8080", "server:app"]