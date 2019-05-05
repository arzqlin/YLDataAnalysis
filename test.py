import numpy as np
from numpy import nan
import seaborn as sns
import pandas as pd
import itertools
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats

df = pd.DataFrame({'x' : [1,None,3,4,5],'y' : [1,2,3,4,5]})
print(df)
df = df.fillna(-9999)
df = df[df.x != -9999]
print(df)

slope, intercept, r_value, p_value, std_err = stats.linregress(df['x'],df['y'])
print(slope, r_value, std_err)