FROM python:3.8-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS deps

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv &&  \
    PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

COPY --from=deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

WORKDIR app/
COPY . .

CMD ["python", "main.py"]
