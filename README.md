# Dockerized Python Application
This project is a Dockerized Python application that includes a Flask backend, MongoDB database, and Nginx reverse proxy. Follow the instructions below to set up and run the application.

## Prerequisites
Before you begin, ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### 1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/niranyadav03/dockerized-python-application.git
cd dockerized-python-application
```
### 2. Build and Start the Containers
Use Docker Compose to build and start the containers:
```bash
docker-compose up --build
```
To stop and remove the containers, use:
```bash
docker-compose down
docker-compose stop(just to stop containers)
```
### 3. Access the App
Once the containers are running, you can access the application via:

Web UI: Open your browser and go to http://localhost. This should display the To-Do List application.
