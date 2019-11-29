#!/bin/sh

### Settings
#
# Source : https://gitlab.com/gitlab-org/omnibus-gitlab/blob/master/README.md

external_url="192.168.99.100"
directory_ssl="/etc/gitlab/ssl/"

### This function start the ssh service.
#
start_ssh() {
    service ssh restart
}

### This function start the gitlab service.
#
start_gitlab() {
    runsvdir-start &
    cp -f /gitlab.rb /etc/gitlab/gitlab.rb
    if [ ! -d $directory_ssl ]
    then
        mkdir -p $directory_ssl
        chmod 700 $directory_ssl
    fi
    if [ ! -f "$external_url.key" ] || [ ! -f "$external_url.crt" ]
    then
        openssl req \
            -x509 \
            -nodes \
            -days 365 \
            -newkey rsa:2048 \
            -keyout $directory_ssl$external_url.key \
            -out $directory_ssl$external_url.crt \
            -subj "/C=FR/ST=IDF/L=Paris/O=42/OU=Org/CN=$external_url"
    fi
    gitlab-ctl reconfigure
}

### Updating Container on start in case is needed.
#
apt-get update -y && apt-get upgrade -y

### See before the differents function use.
#
start_gitlab
start_ssh

### Tail all logs
#
gitlab-ctl tail -f

