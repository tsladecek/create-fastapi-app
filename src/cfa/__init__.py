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
def cfa(
        path: str = typer.Argument(..., help="Directory where the FastAPI app will be initialized"),
        auth: AuthOptions = typer.Option('none',
                                         help="Auth options. Allowed values are: "
                                              "none: for no authentication, "
                                              "self: for self managed authentication and user management, "
                                              "backend: for auth managed by other API")
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

    print(f':oncoming_fist: The project is setup at: {path}')
