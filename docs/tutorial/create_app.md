# Create app

!!! info "tldr"

    ```shell
    cfa create /path/to/app --auth=[none/self/backend]
    ```

---

Once you [installed](../installation.md) the application, create a new app is easy. Simply call:

```shell
cfa create /path/to/app
```

and replace the `/path/to/app` to a destination where you want your app to reside.

## Auth

The app can be initialized in three ways in terms of `auth`:

- `none` - no auth (default)
- `self` - self-managed auth

    ```shell
    cfa create ~/my_fastapi_dir --auth=self
    ```

    Will create a `users` table and auth mechanisms for authorizing requests

- `backend` - auth managed by other backend

    ```shell
    cfa create ~/my_fastapi_dir --auth=backend
    ```

    Will create a logic for authorizing requests via external backend API. Remember to set the `BACKEND_URL` env var, as well as the `GET_USER_BY_TOKEN_ENDPOINT` env variable.

    When trying to authorize, by default the app will call an endpoint at `http://{BACKEND_URL}/{GET_USER_BY_TOKEN_ENDPOINT}/{token}`. Make sure to have this endpoint and it returns a user object (with name, surname, email, etc)

## Git

By default, when running the `cfa create ...` script, a git repo will be initialized in the target directory. If you wish to suppress this option, supply the `--no-git-init` flag.
