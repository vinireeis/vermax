FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock alembic.ini ./

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    postgresql-client && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

RUN poetry install --no-root --no-dev

COPY . .

CMD ["poetry", "run", "python3", "main.py"]
