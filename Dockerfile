FROM ubuntu:latest

WORKDIR /app

ENV PYTHONPATH=/app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml uv.lock /app/

RUN uv sync --locked

COPY . /app/

EXPOSE 8000

CMD ["uv", "run", "fastapi", "dev", "src/app/client.py", "--host", "0.0.0.0", "--port", "8000"]