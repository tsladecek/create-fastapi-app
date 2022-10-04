# FastAPI app

## Requirements
- pipenv

```shell
pip install --user pipenv
```

## Development

1. Install app requirements
    
    ```shell
    pipenv shell
    pipenv sync --dev
    ```
   
2. Initialize database
    
    ```shell
    sh init_db.sh
    ```

3. Run app

    ```shell
    python main.py
    ```
   
The app will run on http://localhost:8000 (by default)

To view the interactive documentation, go to http://localhost:8000/docs

### App requirements 

The application uses [pipenv](https://pipenv.pypa.io/en/latest/) for package management. Make sure that any package related manipulations use `pipenv` command, instead of `pip` !!!

`pipenv` manages the virtual environment on your machine and automatically updates the `Pipfile` and `Pipfile.lock` files. Do not add / remove packages from these files manually!

Here are some helpful commands:

```shell
# Install a package and add it to Pipfile
pipenv install <package_name>

# Install all packages from Pipfile and update Pipfile.lock
pipenv install

# Uninstall a package and remove it from Pipfile
pipenv uninstall <package_name>

# Install all packages specified in Pipfile.lock
pipenv sync
```

### Environment

Application is configurable with a `.env` file. Configurations from this file overwrite configurations in the `app/core/config.py`.

Please make sure to exclude the `.env` file from git (by adding it to the .gitignore).

### Adding new model

When you declare a new SQLAlchemy model in the `app/models` directory, simply run:

```shell
cfa add-model <model_name> <path_to_model_file>
```

This will generate schemas in the `app/schemas` directory, update the `app/schemas/__init__.py` file and create a crud class in `app/crud`.

Make sure install the `create-fastapi-app` in your current environment. To do so, run:

```shell
pipenv install --dev create-fastapi-app
```
