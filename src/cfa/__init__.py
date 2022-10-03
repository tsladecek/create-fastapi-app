import pathlib
import shutil

import typer

app = typer.Typer()


@app.command()
def cfa(
        path: str = typer.Argument(..., help="Directory where the FastAPI app will be initialized")
):
    """
    Create FastAPI app

    Initialize a FastAPI app at specified path
    """
    shutil.unpack_archive(pathlib.PurePath(pathlib.Path(__file__).resolve().parent, 'data', 'cfa.tar'), path)
