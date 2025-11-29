# Use the official Python 3.9 image as the base
FROM python:3.9

# Install required Python packages
RUN pip install pandas sqlalchemy psycopg2-binary fastparquet wget

# Set the working directory inside the container
WORKDIR /app

# Copy the data ingestion script into the container
COPY ingest_data.py ingest_data.py

# Define the default command to run the script
ENTRYPOINT ["python", "ingest_data.py"]