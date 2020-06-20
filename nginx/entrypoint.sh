#!/bin/sh

# Get certs
certbot certonly -n -d staffshare.surge.sh,www.staffshare.surge.sh \
  --standalone --preferred-challenges http --email barkoafrasah@gmail.com --agree-tos --expand

# Kick off cron
/usr/sbin/crond -f -d 8 &

# Start nginx
/usr/sbin/nginx -g "daemon off;"