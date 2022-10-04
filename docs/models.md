# Models manipulation

FastApi works best with pydantic schemas. These should be created for every model in the database as well as a separate crud class.

When creating new model, it can be easy to forget these steps and since they are so repetitive, it is easy to automatize it.

When you declare a new SQLAlchemy model in the `app/models` directory, simply run:

```shell
cfa add-model <model_name> <path_to_model_file>
```

This will generate schemas in the `app/schemas` directory, update the `app/schemas/__init__.py` file and create a crud class in `app/crud`