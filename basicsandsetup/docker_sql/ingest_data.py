#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import argparse
from time import time
import os
import pandas as pd
import fastparquet  # For reading parquet files
from sqlalchemy import create_engine  # For database connection

# Main function to handle data ingestion
def main(params):
    # Extract parameters
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    url=params.url

    # Download the parquet file from the provided URL
    os.system(f"wget {url} -O {params.filename}")

    # Read the parquet file into a DataFrame
    df=pd.read_parquet(params.filename)

    # Create a connection to the PostgreSQL database
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Convert datetime columns to proper format
    df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)

    # Create the table schema in the database
    df.head(n=0).to_sql(name=table_name,con=engine,if_exists="replace")

    # Ingest data in chunks to avoid memory issues
    chunksize = 100000
    for start in range(0, len(df), chunksize):
        t_start = time()
        chunk = df.iloc[start:start+chunksize]
        chunk.to_sql(name=table_name ,con=engine,if_exists="append")
        print(f"Chunk {start//chunksize + 1} ingested in {time() - t_start} seconds")

# Entry point for the script
if __name__ == '__main__':
    # Define command-line arguments
    parser = argparse.ArgumentParser(description='Ingest parquet to postgres database', )
    parser.add_argument('--user',help="user name for postgres")  # PostgreSQL username
    parser.add_argument('--password',help="password for postgres")  # PostgreSQL password
    parser.add_argument('--host',help="host for postgres")  # PostgreSQL host
    parser.add_argument('--port',help="port for postgres")  # PostgreSQL port
    parser.add_argument('--db',help="database name for postgres")  # PostgreSQL database
    parser.add_argument('--table_name',help="table name for postgres")  # PostgreSQL table
    parser.add_argument('--filename',help="parquet file to ingest")
    parser.add_argument('--url',help="url to download parquet file")  # URL to download parquet file
    args = parser.parse_args()

    main(args)


