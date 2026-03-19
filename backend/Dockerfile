FROM python:3.12

WORKDIR /fastapi

# Install uv and sync dependencies (no project install; we copy app next)
COPY pyproject.toml uv.lock ./
RUN pip install uv \
    && uv sync --no-install-project --frozen

ENV VIRTUAL_ENV=/fastapi/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY app ./app
COPY config.py main.py ./

CMD ["python", "main.py"]
