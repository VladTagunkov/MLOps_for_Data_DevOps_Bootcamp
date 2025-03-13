import pickle
import pandas as pd
import numpy as np
import os
import sys



def read_data(filename):
    df = pd.read_parquet(filename)
    categorical = ['PULocationID', 'DOLocationID']
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def load_model_dv():
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv, model


def make_prediction(year,month):
    categorical = ['PULocationID', 'DOLocationID']
    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')
    dv,model = load_model_dv()
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    return model.predict(X_val)


def run():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    prediction = make_prediction(year,month)
    print(np.mean(prediction))

if __name__ == '__main__':
    run()












