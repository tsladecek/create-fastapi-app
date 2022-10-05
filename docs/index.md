# Create FastAPI App

Create and manage FastAPI applications

## Quick Tour

Follow these steps to set up a FastAPI project

### Installation

This is a [pip package](https://pypi.org/project/create-fastapi-app/). Thus, the only thing you need to do, is to run:

```shell
pip install create-fastapi-app
```

### Usage

To create a new applications at a directory `~/my_fastapi_dir`, run:

```shell
cfa create ~/my_fastapi_dir --auth=[none/self/backend]
cd ~/my_fastapi_dir
```

Then install the requirements (expects that you installed [pipenv](https://pipenv.pypa.io/en/latest/) on your system):

```shell
pipenv shell
pipenv sync --dev
```

Initialize the database:

```shell
sh init_db.sh
```

Run the application:

```shell
python main.py
```

Done! You can view the interactivate documentation at [localhost:8000/docs](http://localhost:8000/docs) :sunglasses: