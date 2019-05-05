import numpy as np 
import pandas as pd
from datetime import datetime 




time_hour = pd.date_range(start = '1/1/2011', end = '1/1/2012', freq = 'H', closed='left')


def get_wind():
    wind = pd.read_csv('/Users/ChloeLam/Desktop/ChemProject/2011VOC/wind_data/wind_data_notitle.csv') 
    wind.set_index(time_hour) 
    wind['time_hour'] = time_hour
    del wind['Height']
    del wind['Source']
    del wind['Date']
    del wind['Time']
    wind.set_index('time_hour', inplace = True, drop = True)

    # wind = parse_wind(wind)
    return wind

# not actually needed
def parse_wind(df):
    for index, row in df.iterrows():
        if row['ErrFlag'] < 0:
            df.ix[index, 'm/s'] = np.nan
            df.ix[index, 'Degree'] = np.nan
            df.ix[index, 'ErrFlag'] = np.nan
    return df


if __name__ == '__main__':
    wind = get_wind()

    print(wind.describe())