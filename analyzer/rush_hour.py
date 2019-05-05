import numpy as np
from numpy import nan
import pandas as pd
from datetime import datetime

def rush_hour(df,chem_names):
    time_hour = pd.date_range(start = '1/1/2011 07:00:00', freq = 'H', periods = 5)
    array = time_hour.time

    weekday_df = df.loc[(df['day_of_week'] == 'Weekday') & (df['time_of_day'].isin(array))]
    holiday_df = df.loc[(df['day_of_week'] == 'Holiday') & (df['time_of_day'].isin(array))]
    

    weekday_mean = {}
    holiday_mean = {}
    rush_hour_ratio = {}
    for chem in chem_names:
        weekday_mean[chem] = weekday_df[chem].mean()
        holiday_mean[chem] = holiday_df[chem].mean()
        rush_hour_ratio[chem] = weekday_mean[chem]/holiday_mean[chem]
    
    return rush_hour_ratio

