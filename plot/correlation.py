import numpy as np
from numpy import nan
import seaborn as sns
import pandas as pd
import itertools
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import stats


def correlation(df,chem1, chem2, location):
    df_sum = df['2011-5-16':'2011-9-15'] 
    df_fall = df['2011-9-16':'2011-11-15']
    df_win = df['2011-11-16':'2012-03-15']
    df_spring = df['2011-4-1':'2011-5-15']
    df_spring1 = df['2012-3-16':'2012-3-31']
    df_spring = df_spring.append(df_spring1)
    alpha = 1
    s = 3

    plt.figure(figsize=(11.69,8.27),dpi = 100)
    ax = df_sum.plot.scatter(x=chem1,y=chem2,label = 'Summer',c='DarkBlue',s = s, alpha = alpha)
    df_fall.plot.scatter(x=chem1,y=chem2,label = 'Fall',c='red',s = s, ax = ax, alpha = alpha)
    df_win.plot.scatter(x=chem1,y=chem2,label = 'Winter',c='green',s = s, ax = ax,alpha = alpha)    
    df_spring.plot.scatter(x=chem1,y=chem2,label = 'Spring',c='orange',s = s, ax = ax,alpha = alpha)
    ax.set_xlabel(chem1.capitalize(),fontsize = 14, fontweight = 'bold',labelpad = 4)
    ax.set_ylabel(chem2.capitalize(),fontsize = 14, fontweight = 'bold',labelpad = 4)    
    ax.get_legend().remove()
    plt.tight_layout()
    plt.savefig('./output3/Correlation_{}_{}_{}.png'.format(chem1,chem2,location))
    
    gen_reg(df_win, chem1, chem2, 'Winter')
    gen_reg(df_spring, chem1, chem2, 'Spring')
    gen_reg(df_sum, chem1, chem2, 'Summer')
    gen_reg(df_fall, chem1, chem2, 'Fall')
    

    

def gen_reg(df, chem1, chem2, season):
    df = df.fillna(-9999)
    df = df.loc[df[chem1] != -9999]
    df = df.loc[df[chem2] != -9999]

    slope, intercept, r_value, p_value, std_err = stats.linregress(df[chem1],df[chem2])
    slope = round(slope,2)
    r_sqr = round(r_value**2,2)
    std_err = round(std_err,2)
    print('{}_{}: m = {} ± {} ({})'.format(chem1, season, slope, std_err, r_sqr))
