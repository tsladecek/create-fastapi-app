# App structure

!!! info "tldr"

    ```text
    📦fastapi-app
     ┣ 📂app
     ┃ ┣ 📂api - endpoints
     ┃ ┣ 📂core - configurations
     ┃ ┣ 📂crud - crud
     ┃ ┣ 📂database - database session and base class
     ┃ ┣ 📂models - SQLAlchemy models
     ┃ ┣ 📂schemas - Pydantic schemas
     ┃ ┣ 📂tests - pytest tests
      ...
    ```


---

When you run the [cfa create](create_app.md) command with auth `none` or `backend` options, a following file tree will be created:

```text
📦fastapi-app
 ┣ 📂app
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📂v1
 ┃ ┃ ┃ ┣ 📂endpoints
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜item.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜deps.py
 ┃ ┣ 📂core
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜config.py
 ┃ ┣ 📂crud
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜crud_example.py
 ┃ ┃ ┗ 📜crud_item.py
 ┃ ┣ 📂database
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜initialize.py
 ┃ ┃ ┗ 📜session.py
 ┃ ┣ 📂models
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜example.py
 ┃ ┃ ┗ 📜item.py
 ┃ ┣ 📂schemas
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜example.py
 ┃ ┃ ┗ 📜item.py
 ┃ ┣ 📂tests
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┃ ┣ 📂v1
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┗ 📜test_item.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜conftest.py
 ┃ ┗ 📜__init__.py
 ┣ 📂git_hooks
 ┃ ┣ 📜pre-commit.sh
 ┃ ┗ 📜pre-push.sh
 ┣ 📜.gitignore
 ┣ 📜Dockerfile
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜README.md
 ┣ 📜create_git_hooks.sh
 ┣ 📜db.db
 ┣ 📜docker-compose.yml
 ┣ 📜env_example
 ┣ 📜init_db.sh
 ┗ 📜main.py
```

auth = `self` adds and updates several files:

```shell hl_lines="7 9 10 12 15 20 24 27 29 31 34 40"
📦fastapi-app
 ┣ 📂app
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📂v1
 ┃ ┃ ┃ ┣ 📂endpoints
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📜auth.py
 ┃ ┃ ┃ ┃ ┣ 📜item.py
 ┃ ┃ ┃ ┃ ┗ 📜user.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜deps.py
 ┃ ┣ 📂core
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜config.py
 ┃ ┣ 📂crud
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜crud_item.py
 ┃ ┃ ┗ 📜crud_user.py
 ┃ ┣ 📂database
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜base.py
 ┃ ┃ ┣ 📜initialize.py
 ┃ ┃ ┗ 📜session.py
 ┃ ┣ 📂models
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜item.py
 ┃ ┃ ┗ 📜user.py
 ┃ ┣ 📂schemas
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜auth.py
 ┃ ┃ ┣ 📜item.py
 ┃ ┃ ┗ 📜user.py
 ┃ ┣ 📂tests
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┃ ┣ 📂v1
 ┃ ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┃ ┣ 📜test_item.py
 ┃ ┃ ┃ ┃ ┗ 📜test_user.py
 ┃ ┃ ┃ ┗ 📜__init__.py
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┗ 📜conftest.py
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜utils.py
 ┣ 📜.gitignore
 ┣ 📜Dockerfile
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜README.md
 ┣ 📜create_git_hooks.sh
 ┣ 📜docker-compose.yml
 ┣ 📜env_example
 ┣ 📜init_db.sh
 ┗ 📜main.py
```

## ./

Place for some general files, environment files and other configurations

## ./app/api/

Folder where endpoints should be specified. E.g. to create a new endpoint for table. All endpoints related to a single table should be grouped in the same file, and the router should be then included in the `./app/api/v1/__init__.py` file.  

## ./app/core/

A place for app configurations

## ./app/crud/

Crud classes utilizing models and schemas for a table in the database. Each crud class should inherit from the CRUDBase class which contains some basic methods for:

- creating (`create(db, obj_in)`)
- reading (`read(db, item_id)`, `read_multi(db, offset, limit)`)
- updating (`update(db, item_id, obj_in)`)
- deleting (`delete(db, item_id)`)

objects in the database

## ./app/database/

Database base class `base.py`, which is inherited by the models, and session (`session.py`). The `initialize.py` contains db initialization scripts useful for development. However, in production the tables and migrations should be handled ideally by [alembic](https://alembic.sqlalchemy.org/en/latest/)

## ./app/models/

Database tables models. Simple classes that inherit from the base class specifying the columns, datatypes, indexes, foreign keys etc. For more info see [SQLAlchemy docs](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)

## ./app/schemas/

[pydantic](https://pydantic-docs.helpmanual.io/) schemas declaring data validation. Schemas are used for database manipulations (create, read, update) as well as for validating requests and specifying response schemas. E.g. imagine we would like to add a post endpoint for creating new items in the database (in  the `./app/api/v1/endpoints/item.py` file). It would look something like this:

```python hl_lines="1 3"
@router.post('/', response_model=schemas.Item)
def get_items(
        obj_in: schemas.ItemCreate,
        db: Session = Depends(deps.get_db)
) -> Any:
    return crud_item.create(db=db, obj_in=obj_in)
```

In the first line, we specify the schema of the json object that will be returned to the user. In the third line, we specify what we expect. If the incoming object does not correspond with the schema, the endpoint will throw an Error.

## ./app/tests/

Tests. See pytest for more info. In short, you simply write functions (with the word test in their names - this is very important) in a file with the word test in its name and then include some assertions inside of the functions. Running the command pytest will detect all these functions and run them.

For example to test if `GET item` endpoint works, simply create a file `./app/tests/api/v1/test_item.py` with following content:

```python
from fastapi.testclient import TestClient

from app.core.config import settings


def test_item_get_multi(client: TestClient) -> None:
    """Test the get items endpoint"""
    r = client.get(f"{settings.API_VERSION}/item/")
    assert r.status_code == 200

    all_runs = r.json()
    assert len(all_runs) > 0
```

There are some configurations already in place. See the `app/tests/conftest.py` for more info. You should be fine with the default settings. For more info see the [official documentation](https://docs.pytest.org/en/7.1.x/)
