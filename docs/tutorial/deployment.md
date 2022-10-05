# Deployment

!!! info "tldr"

    ```shell
    docker build -t <image_name>
    docker run <image_name> -p <port>:8000 --env-file .env
    ```

    or 

    ```shell
    docker-compose up
    ```

## Dockerfile

To build a docker image, simply run:

```shell
docker build -t <image_name> .
```

Then to run the application:

```shell
docker run <image_name> -p <port>:8000 --env-file .env
```

Make sure that the database is running and your `.env` file contains correct connection string.

## docker-compose

If you wish to start the app as well as the database, use the `docker-compose.yml` file. Make sure that your `.env` file contains following variables:

- `MARIADB_USERNAME` - sql username
- `MARIADB_PASSWORD` - sql user password
- `DB_NAME` - name of the database
- `DB_DATA` - absolute path to where the database data should be saved
- `SQLALCHEMY_DATABASE_URI` equal to `mysql+pymysql://$MARIADB_USERNAME:$MARIADB_PASSWORD@db:3306/$DB_NAME`

To run the application, simply run:

```shell
docker-compose up
```
