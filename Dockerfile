FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client && \
    pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \

WORKDIR /src

COPY pyproject.toml poetry.lock alembic.ini /src/

RUN poetry install

COPY . /src

CMD ["poetry", "run", "python3", "main.py"]
