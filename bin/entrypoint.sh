#!/bin/sh

# This script ensures we don't try to connect to the
# database before it's up and running
echo "Waiting for postgres..."

while ! nc -z database 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"