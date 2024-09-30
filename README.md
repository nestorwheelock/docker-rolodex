
# Dockerized Rolodex Application

This is a simple Rolodex application that allows you to store and retrieve contacts using a Flask-based API and SQLite database. The application is containerized using Docker.

## Features

- Add and retrieve contacts via a REST API.
- Store contacts in a SQLite database.
- Import contacts from a Google Contacts CSV export.

## Prerequisites

- Docker installed on your machine.
- Python (if you plan to run the scripts outside of Docker).

## Setup and Usage

### 1. Clone the repository

```bash
git clone <repository_url>
cd docker-rolodex
```

### 2. Build the Docker image

```bash
docker build -t rolodex-app .
```

### 3. Run the Docker container

```bash
docker run -d -p 5000:5000 rolodex-app
```

### 4. Import Google Contacts

1. Export your Google Contacts as a CSV file (in Google CSV format).
2. Place the `contacts.csv` file in the project directory.
3. Run the import script inside the Docker container:

```bash
docker run -v $(pwd)/contacts.csv:/app/contacts.csv rolodex-app python import_contacts.py
```

### 5. Access the Rolodex API

- **Add a contact**:
    ```bash
    curl -X POST http://localhost:5000/contacts     -H "Content-Type: application/json"     -d '{"name": "John Doe", "phone": "123-456-7890"}'
    ```

- **Retrieve all contacts**:
    ```bash
    curl http://localhost:5000/contacts
    ```

## Additional Scripts

### `setup-docker-env.sh`

This script automates setting up Docker permissions on your machine. It adds your user to the Docker group and ensures the Docker service is running.

Run it with:
```bash
./setup-docker-env.sh
```

### `build-and-run-docker.sh`

This script automates the process of building the Docker image and running the container. Run it with:

```bash
./build-and-run-docker.sh
```

## License

This project is licensed under the MIT License.