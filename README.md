# Setup
To follow this readme and run this project, first install Docker and docker-compose.
Please note that an IDE is optional.

[Installing docker](https://docs.docker.com/get-docker/)

[Installing docker-compose](https://docs.docker.com/compose/install/)

# Example FastAPI project

## Overview
This project contains a FastAPI, and a postgres DB for the api to interact with. All of this is designed to be run in
docker containers. This is orchestrated with docker-compose and a Makefile.

## Getting started

TLWR: Run `make initialize_pg` then `make api`. Go to `localhost:8000/docs`. Click "Authorize" in the top right. Put in
Username: `test` Password:`test` and the email is `test@gmail.com`. Click around on the routes and try them out.



All the command you will need to use are included in the Makefile. Some example data is included and can be automatically
loaded into dockerized postgres DB. All postgres data is saved in data/postgres and preserved through db shutdowns.

To set up the postgres db with the correct tables, and some example data run `make initialize_pg`.
NOTE: This will delete all changes, including schema and data, made to PG.

To just run the PG migrations (using Alembic) run `make run_migrations`. You can do this after adding new migrations
without modifying the data already in PG (unless your migrations edit the data).

To start the api, PG DB, and link them run `make api`. You can access the API on `localhost:8000` and the api docs on
`localhost:8000/docs` or `localhost:8000/redoc`. The only difference between those are the UI. PG can be accessed on
`localhost:5432` using Username: `test` Password: `test` and DB: `test`. Easy to remember ;)

This project includes production grade auth with username/password and JTWs. To "login" (after running `make initialize_pg`)
you can use Username: `test` Password: `test`. The API docs include auth support, and a fully interactive environment
to interact with the example routes! Give it a try!

If you want to just spin up the PG DB run `make db_only`
