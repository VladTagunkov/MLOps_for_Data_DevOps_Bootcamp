import pandas as pd
from datetime import datetime
import batch

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


def test_prepare_data():
    df = df_creator()
    categorical = ['PULocationID', 'DOLocationID']
    actual_df = batch.prepare_data(df,categorical)
    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime','duration']
    expected_data = [
        ('-1', '-1', dt(1, 1), dt(1, 10), 9.000),
        ('1', '1', dt(1, 2), dt(1, 10), 8.000), 
    ]
    expected_df = pd.DataFrame(expected_data,columns=columns)
    assert actual_df.equals(expected_df)