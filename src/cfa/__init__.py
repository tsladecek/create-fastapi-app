import enum
import pathlib
import subprocess

import typer
from rich import print

from .apply_template_option import apply_template_option

app = typer.Typer()


class AuthOptions(enum.Enum):
    none = 'none'
    backend = 'backend'
    self = 'self'


@app.command()
def version():
    """Application version"""
    print('VERSION') # just a placeholder replaced in CI


@app.command()
def create(
        path: str = typer.Argument(..., help="Directory where the FastAPI app will be initialized"),
        auth: AuthOptions = typer.Option('none',
                                         help="Auth options. Allowed values are: "
                                              "none: for no authentication, "
                                              "self: for self managed authentication and user management, "
                                              "backend: for auth managed by other API"),
        git_init: bool = typer.Option(True, help='Initialize git repository')
):
    """
    Create FastAPI app

    Initialize a FastAPI app at specified path
    """
    print(':flexed_biceps: Creating Project')
    subprocess.run(['cp', '-r', pathlib.PurePath(pathlib.Path(__file__).resolve().parent, 'fastapi-app'), path])

    if auth in [AuthOptions.self, AuthOptions.backend]:
        print(f':locked_with_key: Setting up Auth to "{auth.name}"')
        apply_template_option('auth', auth.name, path)

    if git_init:
        print(':wrench: Initializing git repo')
        subprocess.run(['git', 'init', path])
    print(f':oncoming_fist: The project is setup at: {path}')


@app.command()
def add_model(
        model_name: str = typer.Argument(..., help='Model name - Case sensitive'),
        model_filepath: str = typer.Argument(..., help='Path to the model file. Relative or absolute'),
):
    """
    Create schemas and crud for a SQLAlchemy model
    """
    path = pathlib.PurePath(model_filepath).parts

    # get app dir for creating schemas and crud
    if len(path) == 1:
        app_dir = '..'
    elif len(path) == 2:
        app_dir = '.'
    else:
        app_dir = pathlib.PurePath(*path[:-2])

    # read models file
    with open(model_filepath, 'r') as f:
        model_file = f.readlines()

    # get columns
    cols = []
    i = 0
    for i, line in enumerate(model_file):
        if line.startswith(f'class {model_name}'):
            i += 1
            break

    datatypes = {
        'string': 'str',
        'text': 'str',
        'integer': 'int',
        'float': 'float',
        'boolean': 'bool',
        'datetime': 'datetime.datetime',
        'date': 'datetime.date',
        'time': 'datetime.time'
    }

    for line in model_file[i:]:
        # break if outside the function
        if line[0] == '\n':
            continue
        elif line[0] != ' ':
            break
        else:
            # infer python datatype from sql datatypes
            if 'Column' in line:
                column_name, spec = line.strip().lower().replace(' ', '').split('=column')
                dt = ''
                for sql_dt, py_dt in datatypes.items():
                    if sql_dt in spec:
                        dt = py_dt
                        break
                cols.append([column_name, dt])

    # Create schemas file
    schemas = [
        'from pydantic import BaseModel\n\n'
        f'class {model_name}Base(BaseModel):',
        '\n'.join(f'    {col}: {dt}' if type != '' else f'    {col}' for col, dt in cols),
        '\n\n'
        f'class {model_name}Create({model_name}Base):',
        '    pass\n\n',
        f'class {model_name}Update({model_name}Create):',
        '    pass\n\n',
        f'class {model_name}InDB({model_name}Base):',
        '    id: int\n',
        '    class Config:',
        '        orm_mode = True\n\n',
        f'class {model_name}({model_name}InDB):',
        '    pass\n'
    ]

    if sum(dt in ['datetime.datetime', 'datetime.time', 'datetime.date'] for _, dt in cols) > 0:
        schemas = ['import datetime\n\n'] + schemas

    # Create schemas file
    with open(pathlib.PurePath(app_dir, 'schemas', path[-1]), 'w') as f:
        f.write('\n'.join(schemas))

    # update schemas/__init__.py
    with open(pathlib.PurePath(app_dir, 'schemas', '__init__.py'), 'a') as f:
        f.write(f'\nfrom {path[-1].split(".")[0]} import {model_name}, {model_name}Create, {model_name}Update\n')

    # Create crud
    crud = [
        "from app import models, schemas",
        "from app.crud.base import CRUDBase\n\n",
        f"class CRUD{model_name}(CRUDBase[models.{model_name}, "
        f"schemas.{model_name}Create, schemas.{model_name}Update]):",
        "    pass\n\n",
        f"crud_{model_name.lower()} = CRUD{model_name}(models.{model_name})\n"
    ]

    # Create crud file
    with open(pathlib.PurePath(app_dir, 'crud', f'crud_{path[-1]}'), 'w') as f:
        f.write('\n'.join(crud))

    print(":panda_face: created [bold yellow]schemas[/bold yellow] at: "
          f"[bold green]{pathlib.PurePath(app_dir, 'schemas', path[-1])}[/bold green] "
          "and [bold red]crud[/bold red] at: "
          f"[bold green]{pathlib.PurePath(app_dir, 'crud', f'crud_{path[-1]}')}[/bold green]")
