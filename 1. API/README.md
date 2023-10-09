
# 1. APP

Here we have different folders and files:

- app with the files with the API code
- tests with different tests
- docker-compose.yaml in order to run the app locally
- Dockerfile and Dockerfile.postgres to build the images for both the app and the db
- gunicorn-cfg.py and run.py used to run the API
- init.sql to create the table in the postgres db
- requirements.py with the needed packages that need to be installed
## Run locally

You can run the app locally simply executing

```bash
  docker-compose up -d
```

## Running Tests

To run tests, run the following command

```bash
  python3 -m unittest tests.tests_app
```

