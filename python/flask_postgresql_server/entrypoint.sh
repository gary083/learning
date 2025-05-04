#!/bin/sh
set -e

# Migrate the database schema.
flask db upgrade

# Start the server.
exec gunicorn "app:create_app()" -b 0.0.0.0:8080 -w 1 --log-level debug