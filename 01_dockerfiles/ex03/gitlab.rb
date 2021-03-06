#Set external_url
external_url "https://192.168.99.107/"         # Must specifie https protocol.

### Nginx configuration
#
# ssl certificate location
nginx['ssl_certificate'] = "/etc/gitlab/ssl/192.168.99.107.crt"
nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/192.168.99.107.key"
#
# by default if external_url is on https, http is disable.
nginx['redirect_http_to_https'] = true
nginx['redirect_http_to_https_port'] = 80
