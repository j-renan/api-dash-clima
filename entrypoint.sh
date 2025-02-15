#!/bin/sh
#if [ -f "/app/.env" ]; then
#    export $(grep -v '^#' /app/.env | xargs)
#fi
#exec "$@"

set -o allexport
[ -f "/etc/secrets/.env" ] && source /etc/secrets/.env
set +o allexport
exec "$@"

