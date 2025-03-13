import pandas as pd
from datetime import datetime
import os

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

def df_creator():
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    return pd.DataFrame(data, columns=columns)

def df_s3_writer():
    df_input = df_creator()
    endpoint_url = os.getenv("S3_ENDPOINT_URL")
    options = {
    'client_kwargs': {
        'endpoint_url': endpoint_url
    }
    }
    input_file = "s3://nyc-duration/yellow_tripdata_2023-01.parquet"

    df_input.to_parquet(
        input_file,
        engine='pyarrow',
        compression=None,
        index=False,
        storage_options=options
)
    

df_s3_writer()