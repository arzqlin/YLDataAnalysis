import numpy as np 
import pandas as pd
from datetime import datetime 

s = pd.Series(np.random.randn(5), index = ['a', 'b', 'c', 'd', 'e'])


d = {   'one': [1,2,3,4],
        'two': [5,6,7,8],
    }
df = pd.DataFrame(d, index = ['a','b','c','d'])





time_hour = pd.date_range(start = '1/1/2011', end = '1/1/2012', freq = 'H', closed='left')
time_half_hour = pd.date_range(start = '1/1/2011', end = '1/1/2012', freq = '0.5H', closed='left')


wind = pd.read_csv('/Users/ChloeLam/Desktop/ChemProject/2011VOC/wind_data/wind_data_notitle.csv') 
wind.set_index(time_hour) 
wind['time_hour'] = time_hour
del wind['Height']
del wind['Source']
del wind['Date']
del wind['Time']
wind.set_index('time_hour', inplace = True, drop = True)


print(wind.head(4))
# print(wind.at[8,'m/s']) # get data at index 8, column m/s

  





