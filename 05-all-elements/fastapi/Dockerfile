FROM python:3.11-bookworm

WORKDIR /app

# Install Poetry
RUN pip install --upgrade pip setuptools \
    && pip install poetry

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Install dependencies globally (no venv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Ensure uvicorn is installed
RUN pip install uvicorn

# Copy app code
COPY voip2_backend voip2_backend

ENV PYTHONPATH=/app
EXPOSE 8080

# Run FastAPI
CMD ["python", "-m", "uvicorn", "voip2_backend.main:app", "--host", "0.0.0.0", "--port", "8080"]
