# Theatre API Service

This repository contains a Theatre API service built using Django Rest Framework (DRF) 
and Dockerized for easy deployment. The API service allows users to manage theatre-related 
data such as actors, genres, plays, performances, reservations, and tickets. The Docker 
setup ensures that the application can run consistently across different environments 
and can be easily deployed in production.

## Features
The API service provides the following features:

* CRUD operations for actors, genres, plays, performances, reservations, and tickets.
* User authentication and authorization using JWT (JSON Web Tokens).
* Uploading and managing play images.
* Seat validation based on the theatre hall's capacity when creating tickets.
* Dockerized for easy deployment and scaling.


## Prerequisites

Before running the Theatre API service in Docker, ensure you have the following installed on your machine:
* Docker: [Install Docker](https://docs.docker.com/get-docker/)
* Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started
1. Clone the repository to your local machine:
```
git clone https://github.com/kamilla-boiko/theatre-api.git
cd theatre-api
```

2. Create a .env file based on the provided .env_sample and update the necessary environment variables.

3. Build the Docker containers and start the application:
```
docker-compose up -d --build
```

## Environment variables

This project uses environment variables to store sensitive or configurable data.
The variables are stored in a file named .env, which should be created in the
project's root directory.
Please follow the instructions below to set up the environment variables for your local development.

### .env file

Create a file named .env in the root directory of the project and add the following variables
with their corresponding values.
* Note: Make sure to keep the .env file secure and do not commit it to the repository.

### .env_sample file

A file named .env_sample is included in the repository as a template for setting up the .env file.
It contains the names of the environment variables without their values.
You can use it as a reference when creating your own .env file.

## API Documentation

The API documentation (Swagger/OpenAPI) can be accessed at 
http://localhost:5432/api/doc/swagger/ or http://localhost:5432/api/doc/redoc/.

## Authentication

The API service uses JWT for user authentication. To access protected endpoints, 
include the JWT token in the Authorization header as follows:
```
Authorization: Bearer your_jwt_token
```

To obtain a JWT token, make a POST request to /api/user/token/ with your email and password.

