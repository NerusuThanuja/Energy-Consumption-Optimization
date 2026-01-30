import pandas as pd
import numpy as np

def load_and_preprocess(path):
    df = pd.read_csv(path, sep=';', na_values='?', low_memory=False)

    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
    df = df[['DateTime', 'Global_active_power']]
    df.dropna(inplace=True)

    df.set_index('DateTime', inplace=True)
    hourly = df.resample('H').mean()
    hourly.columns = ['energy']

    hourly.replace([np.inf, -np.inf], np.nan, inplace=True)
    hourly.dropna(inplace=True)

    return hourly