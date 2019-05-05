import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_ssl_diurnal(df1, df2, chemical, location):
    # initiate plot 
    fig = plt.figure(figsize=(5,4), dpi = 150)

    # initiate sub 1
    sub1 = fig.add_subplot(211)

    # set title
    if location == 'YL':
        sub1.set_title(chemical.capitalize(),fontsize = 14, fontweight = 'bold')
    
    if location == 'MK':
        sub1.set_title(chemical.capitalize(),fontsize = 14, fontweight = 'bold')
    
    # plot sub 1
    subplot_diurnal(sub1, df1, chemical, 'Hour (Summer)',2)
    
    # initiate sub 2
    sub2 = fig.add_subplot(212) 
    # plot sub 2
    subplot_diurnal(sub2, df2, chemical, 'Hour (Winter)',2)


    # adjust y axis
    ylimit1 = sub1.get_ylim()
    ylimit2 = sub2.get_ylim()
    ylimit = max(ylimit1[1],ylimit2[1])
    sub1.set_ylim(0, ylimit) 
    sub2.set_ylim(0, ylimit) 
   
    plt.tight_layout(w_pad = 1,h_pad = 1)

def plot_ttl_diurnal(df, chemical, location):

    fig = plt.figure(figsize=(5,4),dpi = 150)
    sub = fig.add_subplot(111)
    if location == 'YL':
        sub.set_title(chemical.capitalize(),fontsize = 14, fontweight = 'bold')
    
    if location == 'MK':
        sub.set_title(chemical.capitalize(),fontsize = 14, fontweight = 'bold')
    
    subplot_diurnal(sub, df, chemical, 'Hour', 1)

    sub.set_ylim(0,)

    plt.tight_layout(h_pad = 1)


def subplot_diurnal(sub, df, chemical, xlabel, graph_count):

    time_axis = []
    for i in range(12):
        time_axis.append(2 * i)
        time_axis.append('')

    try:
        if graph_count == 1:
            sub = sns.pointplot(x = 'time_of_day', y = chemical, hue = "day_of_week", palette = ['#013326','#b63f00'], data = df, linestyles='-', scale= 0.8, markers=['o', 'v'], legend_out = True,errwidth=0, capsize=0)
        else:
            sub = sns.pointplot(x = 'time_of_day', y = chemical, hue = "day_of_week", palette = ['#013326','#b63f00'], data = df, linestyles='-', scale= 0.5, markers=['o', 'v'], legend_out = True,errwidth=0, capsize=0)
    except:
        pass

    sub = sns.boxplot(x = 'time_of_day', y = chemical, hue = "day_of_week", palette = 'Set3', data = df, showfliers = False, whis=[5, 95],linewidth = 0.8)
    sub.set_xlabel(xlabel,fontsize = 10,fontweight = 'bold',labelpad = 4)
    sub.set_ylabel('  ',fontsize = 10)    
    sub.set_xticklabels(time_axis) 
    sub.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    sub.set_axisbelow(True)
    sub.legend(fancybox=True, loc='upper left', borderpad=1, framealpha=0.5)
    # sub.legend_.remove()
    

def plot_diurnal_ARCHIVE(df1, df2, chemical):

    # get x ticks    
    time_half_hour = pd.date_range(start = '1/1/2011', end = '1/2/2011', freq = 'H', closed='left')
    time_half_hour = time_half_hour.time

    minor_time = []
    for value in time_half_hour:
        minor_time.append(str(value)[:-3])

    major_time = minor_time[0 :: 8]



    # initiate plot 

    fig = plt.figure(figsize=(20, 10))

    

    # sub 1
    sub1 = fig.add_subplot(211)
    # for MK
    # sub1.set_title('Diurnal variation of {} at MK Station - 4/2011 to 3/2012'.format(chemical.capitalize()),fontsize = 20)
    # for YL
    sub1.set_title('Diurnal variation of {} at YL Station - 1/2011 to 12/2011'.format(chemical.capitalize()),fontsize = 20, fontweight = 'bold')

    sub1 = sns.pointplot(x = 'time_of_day', y = chemical, hue = "day_of_week", palette = ['#013326','#b63f00'], data = df1, linestyles='-', scale= 0.8, markers='x', errwidth=0, capsize=0)
    sub1 = sns.boxplot(x = 'time_of_day', y = chemical, hue = "day_of_week", palette = 'Set3', data = df1, showfliers=True, fliersize=1, linewidth = 0.8)
    
    sub1.set_xlabel('Hour (Summer)',fontsize = 16)
    sub1.set_ylabel('Concentration (ppbv)',fontsize = 16)
    ylimit1 = sub1.get_ylim()
    sub1.set_xticklabels(minor_time, rotation=45) 
    sub1.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1)
    sub1.set_axisbelow(True)
    sub1.legend(fancybox=True, loc='upper left', borderpad=1, framealpha=0.5)

    # sub 2
    sub2 = fig.add_subplot(212) 

    try:
        sub2 = sns.pointplot(x = 'time_of_day', y = chemical, hue = "day_of_week", palette = ['#013326','#b63f00'], data = df2, linestyles='-', scale= 0.8, markers='x', errwidth=0, capsize=0)
    except:
        pass
    sub2 = sns.boxplot(x = 'time_of_day', y = chemical, hue = "day_of_week", palette = 'Set3', data = df2, showfliers=True, fliersize=1, linewidth = 0.8)
    sub2.set_xlabel('Hour (Winter)',fontsize = 16)
    sub2.set_ylabel('Concentration (ppbv)',fontsize = 16)
    ylimit2 = sub2.get_ylim()
    sub2.set_xticklabels(minor_time, rotation=45) 
    sub2.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    sub2.set_axisbelow(True)
    sub2.legend(fancybox=True, loc='upper left', borderpad=1, framealpha=0.5)


    # adjust y axis
    ylimit = max(ylimit1[1],ylimit2[1])
    sub1.set_ylim(-0.01, ylimit) 
    sub2.set_ylim(-0.01, ylimit) 
   
    plt.tight_layout(pad = 3 , w_pad = 2, h_pad = 4)

