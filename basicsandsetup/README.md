# Basics and Setup

This folder contains introductory assignments and code for learning Docker and Terraform. Below is a summary of the tasks and key learnings:

## Docker Assignments

### 1. Setting up PostgreSQL and pgAdmin using Docker Compose
- **File**: [`docker_sql/docker-compose.yaml`](docker_sql/docker-compose.yaml)
- **Description**: Sets up a PostgreSQL database and pgAdmin for managing the database.
- **Key Learnings**:
  - Using Docker Compose to define multi-container applications.
  - Networking between containers using `pg-network`.

### 2. Manual Docker Commands
- **File**: [`docker_sql/docker_networkpg`](docker_sql/docker_networkpg)
- **Description**: Demonstrates manually creating a Docker network and running PostgreSQL and pgAdmin containers.
- **Key Learnings**:
  - Running containers with environment variables.
  - Volume mapping for data persistence.
  - Networking containers manually.

### 3. Data Ingestion with Docker
- **Files**: 
  - [`docker_sql/ingest_data.py`](docker_sql/ingest_data.py)
  - [`docker_sql/pipeline.py`](docker_sql/pipeline.py)
  - [`docker_sql/Dockerfile`](docker_sql/Dockerfile)
- **Description**: Scripts and Dockerfile for ingesting data into the PostgreSQL database.
- **Key Learnings**:
  - Building custom Docker images using a `Dockerfile`.
  - Running Python scripts inside Docker containers.

### 4. Data Upload Notebook
- **File**: [`docker_sql/data_upload.ipynb`](docker_sql/data_upload.ipynb)
- **Description**: Demonstrates data processing and uploading to the database using Python.
- **Key Learnings**:
  - Using Python libraries like `pandas` and `sqlalchemy` for data manipulation and database interaction.

## Terraform Assignments

### 1. Google Cloud Storage Bucket
- **File**: [`terraform/main.tf`](terraform/main.tf)
- **Description**: Creates a GCS bucket with lifecycle rules.
- **Key Learnings**:
  - Defining resources in Terraform.
  - Using lifecycle rules for automatic data management.

### 2. BigQuery Dataset
- **File**: [`terraform/main.tf`](terraform/main.tf)
- **Description**: Creates a BigQuery dataset.
- **Key Learnings**:
  - Managing Google Cloud resources with Terraform.
  - Using variables for dynamic configurations.

---

This folder serves as a foundational step in understanding Docker and Terraform for data engineering tasks.