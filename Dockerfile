FROM python:3.12.5-alpine3.19

WORKDIR /app 
EXPOSE 8000
COPY requirements.txt /app
RUN apk add --no-cache postgresql-libs && \
RUN pip3 install -r requirements.txt --no-cache-dir
RUN django-admin startproject luna_watch .
RUN django-admin startapp app_luna_watch
COPY ./luna_watch luna_watch/
COPY ./app_luna_watch app_luna_watch/

CMD ["python", "manage.py", "runserver"]
