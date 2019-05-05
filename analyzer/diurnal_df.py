import pandas as pd 
import numpy as np
from datetime import datetime

    
#returns 
def sample_time(ts, time):
    return list(ts.at_time(time))  # returns the Series of this chemical at a specific time





    
    
    
    
    
    time_dr = pd.date_range(start = '1/1/2011', end = '2/1/2011', freq = '0.5H', closed='left')

    half_hour = time_dr.time

    new_df = pd.DataFrame(columns = half_hour)


