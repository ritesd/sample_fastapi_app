# PREQUIEN_TEST Project

## Description

This is a FastAPI project that demonstrates how to create a simple RESTful API with user authentication, SQLite database integration, and Docker setup.

## Features

- User registration and authentication.
- Endpoint for generating a random 500-dimensional array of floats from an input sentence.
- Docker setup for containerization.

## Prerequisites

- Python 3.8 or higher
- Poetry (for managing dependencies)
- Docker (if you want to run the application in a Docker container)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/ritesd/prequien_test.git

2. Change the working directory
   ```shell
   cd preuien_test

3. Change the working directory
   ```shell
   poetry install

## Configuration

1. Create a .env file in the project directory and set your environment variables. You can use the .env.example file as a template.
	```shell
	cp .env.example .env

## Usage

### Running the FastAPI Application Locally
1. Activate the Poetry virtual environment:
	```shell
	poetry shell

2. Start the FastAPI application:
	```shell
	uvicorn src.app.main:app --host 0.0.0.0 --port 8000

3. For testing the application:
	```shell
	pytest

#### The application will be accessible at http://localhost:8000.

## Running the FastAPI Application in Docker

1. Build a Docker image for the project:

	```shell
	Copy code
	docker build -t prequien_test .

2. Start a Docker container with the FastAPI application:

	```shell
	Copy code
	docker run -d -p 8000:8000 prequien_test

3. If you want to build and run using docker-compose

	```shell
	docker-compose -f docker_compose.yml up -d --build

#### The application will be accessible at http://localhost:8000.

## API Documentation
- Swagger documentation is available at http://localhost:8000/docs
- ReDoc documentation is available at http://localhost:8000/redoc

## License
This project is licensed under the MIT License. See the [MIT License](LICENSE)
 file for details.
