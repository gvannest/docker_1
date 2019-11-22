FROM nginx:1.17-alpine

RUN apk add bash

RUN adduser -S -G www-data www-data
RUN rm /etc/nginx/conf.d/default.conf

COPY app.conf /etc/nginx/conf.d/
