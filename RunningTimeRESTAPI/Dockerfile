FROM python:3.6-slim-buster

RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app/
ADD runningTimeRESTAPI /app/

ENV PORT=8888

RUN pip install -r requirements.txt

EXPOSE 8888
CMD gunicorn runningTimeRESTAPI.wsgi:application --bind 0.0.0.0:$PORT
