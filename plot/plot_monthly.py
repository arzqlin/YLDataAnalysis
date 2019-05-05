import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_monthly(main_df, chemical, location):
    df = main_df
    # initiate plot 
    fig = plt.figure(figsize=(11.69,8.27))

    # initiate sub
    sub = fig.add_subplot(111)
    # if location == 'YL':
    #     sub.set_title('Monthly concentration of {} at YL Station'.format(chemical.capitalize()),fontsize = 14, fontweight = 'bold')

    subplot_monthly(sub, df, chemical)

    plt.tight_layout(w_pad = 2, h_pad = 2)


def subplot_monthly(sub, df, chemical):
    # get x ticks    
    time_axis = ['Apr-11', 'May-11', 'June-11', 'July-11', 'Aug-11', 'Sept-11', 'Oct-11', 'Nov-11', 'Dec-11','Jan-12','Feb-12','Mar-12']

    qualitative_colors = sns.color_palette("Set3", 10)
    set1_color = sns.color_palette("Set1", 1)

    try:
        sub = sns.pointplot(x = 'month', y = chemical, linestyles = '--', linewidth = 0.8, color = set1_color[0], data = df, scale= 1, markers='o', errwidth=0, capsize=0, )
    except:
        pass
    sub = sns.boxplot(x = 'month', y = chemical, data = df, showfliers=False, linewidth = 0.8, color = qualitative_colors[4],width = 0.5)
    sub.set_xlabel('Month',fontsize = 12,fontweight = 'bold')
    sub.set_ylabel('Concentration (ppbv)',fontsize = 12, fontweight = 'bold')    
    sub.set_xticklabels(time_axis, rotation=45,) 
    sub.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    sub.set_axisbelow(True)


    sub.set_ylim(0, sub.get_ylim()[1])

    
