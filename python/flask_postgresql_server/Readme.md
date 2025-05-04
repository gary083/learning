# Document for myself

### Setup PostgreSQL database

```shell
# Installation
$ apt install postgresql postgresql-client

# Setup
$ sudo -iu postgres psql
psql (17.2 (Debian 17.2-1+build9))
Type "help" for help.

postgres=# CREATE ROLE myuser WITH LOGIN PASSWORD 'mypass';
CREATE ROLE
postgres=# CREATE DATABASE mydb OWNER myuser;
CREATE DATABASE
postgres=# \q

# Check the database.
$ psql "postgresql://myuser:mypass@localhost/mydb" -c '\dt'
```

### Model Migration

```shell
# Initialize migration.
$ FLASK_APP=app:create_app flask db init

# Check the latset mode and create the migration script.
$ FLASK_APP=app:create_app flask db migrate -m "initial schema"

# Migrate the model.
$ FLASK_APP=app:create_app flask db upgrade
```

### Create local server for testing

```shell
$ gunicorn --workers 1 --bind 127.0.0.1:8080 "app:create_app()"

```

(on another terminal)

```shell
$ curl -X POST http://127.0.0.1:8080/data -H "Content-Type: application/json" -d '{"key1": "value1", "key2": 123}'
```
