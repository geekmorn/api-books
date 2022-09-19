# API Books

## Run

1. Set up .env file use [env-example](./env-example)

2. [Docker-compose](https://docs.docker.com/compose/) is used to run the API.

```bash
docker-compose up
```

> Each time a new container is created, it needs to be reloaded. Because when the database is created again, the application fails to connect to the database, which requires the container to be restarted.

## Development

1. Set up a database.

2. Activate [pipenv](https://pipenv.pypa.io/en/latest/) environment or any other

```bash
pipenv shell
```

3. Install dependencies

```bash
pipenv install
# or
pip install -r requirements.txt
```

4. Set up .env file use [env-example](./env-example)

    <!-- > <sub>To run in a container, POSTGRES_HOST use the name of the database container -->

    > To run on a localhost, POSTGRES_HOST uses the name "localhost". To run in docker-compose use the name of the database container.

5. Run application

```bash
python -m run
```

## Tech stack

-   [Python](https://www.python.org/)
-   [FastAPI](https://fastapi.tiangolo.com/)

## Database

-   [PostgreSQL](https://www.postgresql.org/)
