FROM mambaorg/micromamba

WORKDIR /app
COPY env.yml /app/env.yml
RUN micromamba create -f env.yml
COPY pyproject.toml /app/pyproject.toml
COPY poetry.lock /app/poetry.lock
RUN micromamba run -n scripts poetry install --with dev