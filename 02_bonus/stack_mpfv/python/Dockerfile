FROM python:3.7-alpine

RUN apk add --no-cache \
	gcc \
	build-base \
	linux-headers \
	python3-dev \
	uwsgi-python3 \
	libffi-dev \
	libressl-dev \
	bash

RUN addgroup -S www-data && adduser -S -G www-data www-data

WORKDIR /python

COPY . /python

RUN pip install -r requirements.txt

RUN chown -R www-data:www-data /var/log 
RUN chmod -R 770 /var/log

USER www-data:www-data

CMD ["uwsgi", "app.ini"]
