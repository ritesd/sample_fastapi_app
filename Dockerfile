# Use an official Python runtime as a parent image
FROM python:3.11

# Below is for postgres
RUN apt-get update &&\
    apt-get upgrade &&\
    apt-get install -y curl build-essential &&\
    apt install -y python3-dev &&\
    apt install -y libpq-dev
# Set the working directory in the container
WORKDIR /app

# Copy only the `pyproject.toml` and `poetry.lock` files to the container
COPY pyproject.toml poetry.lock /app/

# Install Poetry globally
RUN pip install poetry

# Install dependencies using Poetry (with no interaction)
RUN poetry lock
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Copy the rest of the application code into the container at /app
COPY . /app/

RUN python src/app/db_setup.py
# Expose the port that the application will run on
EXPOSE 8000

# Define the command to run your FastAPI application
CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
