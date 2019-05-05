import pandas as pd

def merge_dataframe(df1, df2):

    result = pd.concat([df1, df2],axis=1)
    return result

