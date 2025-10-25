#!/usr/bin/env python
# coding: utf-8

import argparse
from time import time
import os
import pandas as pd
import fastparquet  
from sqlalchemy import create_engine

def main(params):
    user=params.user
    password=params.password
    host=params.host
    port=params.port
    db=params.db
    table_name=params.table_name
    url=params.url
    os.system(f"wget {url} -O {params.filename}")
    df=pd.read_parquet(params.filename)
    
    
    
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)
    df.head(n=0).to_sql(name=table_name,con=engine,if_exists="replace")
    chunksize = 100000
    for start in range(0, len(df), chunksize):
        t_start = time()
        chunk = df.iloc[start:start+chunksize]
        chunk.to_sql(name=table_name ,con=engine,if_exists="append")
        print(f"Chunk {start//chunksize + 1} ingested in {time() - t_start} seconds")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest parquet to postgres database', )
    #user, password, host, port, db, table_name, filename
    parser.add_argument('--user',help="user name for postgres")           # positional argument
    parser.add_argument('--password',help="password for postgres")           # positional argument
    parser.add_argument('--host',help="host for postgres")           # positional argument
    parser.add_argument('--port',help="port for postgres")           # positional argument
    parser.add_argument('--db',help="database name for postgres")           # positional argument
    parser.add_argument('--table_name',help="table name for postgres")           # positional argument
    parser.add_argument('--filename',help="parquet file to ingest")
    parser.add_argument('--url',help="url to download parquet file")           # positional argument
    args = parser.parse_args()

    main(args)


