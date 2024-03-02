FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD gunicorn marketplace.wsgi.application --bind 0.0.0.0:8000 --workers 4
