import numpy as np
import pandas as pd
# from .mean_pct import data_avg
# from .sd_sem import sd

def del_spikes(df):

    for col in list(df.columns):
        col_limit = 3 * df.std(0)[col] + df.mean(0)[col]
        for row in list(df.index.values):      
            if df.at[row, col] > col_limit:
                # print('value at row {}, col{} ： {} has be deleted, col_limit here is {}'.format(row, col, df.at[row, col],col_limit))
                df.at[row, col] = None

    return df

