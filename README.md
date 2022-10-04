# Create FastAPI App (cfa)

Create and manage FastAPI applications

## Quick Tour

Follow these steps to set up a FastAPI project. See the [documentation](https://tsladecek.github.io/create-fastapi-app/) for more details.

### Installation

This is a [pip package](https://pypi.org/project/create-fastapi-app/). Thus, the only thing you need to do, is to run:

```shell
pip install create-fastapi-app
```

### Usage

To create a new applications at a directory `~/my_fastapi_dir`, run:

```shell
cfa create ~/my_fastapi_dir
```

#### Options

##### Auth

You can choose from three auth setups:

- none - no auth (default)
- self - self-managed auth

    ```shell
    cfa create ~/my_fastapi_dir --auth=self
    ```

    Will create a `users` table and auth mechanisms for authorizing requests

- backend - auth managed by other backend

    ```shell
    cfa create ~/my_fastapi_dir --auth=backend
    ```

    Will create a logic for authorizing requests via external backend API. Remember to set the `BACKEND_URL` env var, as well as the `GET_USER_BY_TOKEN_ENDPOINT` env variable.

    When trying to authorize, by default the app will call an endpoint at `http://{BACKEND_URL}/{GET_USER_BY_TOKEN_ENDPOINT}/{token}`. Make sure to have this endpoint and it returns a user object (with name, surname, email, etc)
