import numpy as np
from numpy import nan
import pandas as pd
import itertools
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cm
plt.rcParams.update({'figure.max_open_warning': 0})
from matplotlib.backends.backend_pdf import PdfPages
import fpdf

from analyzer.merge_dataframe import merge_dataframe
from analyzer.get_chemicals import get_chemicals, chem_names
from analyzer.get_wind import get_wind
from analyzer.holiday import get_holiday
from analyzer.rush_hour import rush_hour

from plot.plot_monthly import plot_monthly
from plot.plot_diurnal import plot_ssl_diurnal, plot_ttl_diurnal
from plot.plot_rose import plot_rose
from plot.comparison import comparison
from plot.get_mixing_ratio import get_mixing_ratio
from plot.correlation import correlation
from plot.get_mir import get_mir
from plot.get_ofh import get_ofh


def monthly(chemical,location):
    fig = plot_monthly(main_df,chemical, location)
    # plt.savefig('{}_plot'.format(chemical))
    return fig

def ssl_diur(chemical,location):
    fig = plot_ssl_diurnal(summer_df, winter_df,chemical, location)
    # plt.savefig('{}_plot'.format(chemical))
    return fig

def ttl_diur(chemical,location):
    fig = plot_ttl_diurnal(main_df,chemical, location)
    # plt.savefig('{}_plot'.format(chemical))
    return fig

def rose(chemical,location):
    fig = plot_rose(rose_df, chemical)
    # plt.savefig('{}_rose'.format(chemical))
    return fig
    
def plot_all(location):
    if location == 'YL':
        for chemical in chem_names:   
            monthlyfig = monthly(chemical,location)
            plt.savefig('./output{}/{}_monthly_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M")))
            
            ssldiurfig = ssl_diur(chemical, location) 
            plt.savefig('./output{}/{}_ssl_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M")))
            
            ttldiurfig = ttl_diur(chemical, location) 
            plt.savefig('./output{}/{}_ttl_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M")))
            
            # rosefig = rose(chemical,location) 
            # pp.savefig(rosefig)
                
    if location == 'MK':
        for chemical in chem_names:   
            monthlyfig = monthly(chemical,location)
            plt.savefig('./output{}/{}_monthly_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M")))
            
            ssldiurfig = ssl_diur(chemical, location) 
            plt.savefig('./output{}/{}_ssl_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M")))
            
            ttldiurfig = ttl_diur(chemical, location) 
            plt.savefig('./output{}/{}_ttl_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M"))) 

def plot_seasonal_ratio(location):
    ratio_mean_dic = {}
    ratio_median_dic = {}

    for chem in chem_names:
        if summer_df[chem].mean() == 0 or winter_df[chem].mean() ==  0:
            ratio_mean = 'N/A'       
        else:
            ratio_mean = round(summer_df[chem].mean()/winter_df[chem].mean() , 2)

        if summer_df[chem].median()== 0 or winter_df[chem].median() == 0:
            ratio_median = 'N/A'
        else:
            ratio_median = round(summer_df[chem].median()/winter_df[chem].median(),  2)

        ratio_mean_dic[chem] = ratio_mean
        ratio_median_dic[chem] = ratio_median

    print(ratio_mean_dic['isoprene'])
    ratio_mean_dic.pop('isoprene')
    ratio_median_dic.pop('isoprene')
    sorted_ratio_mean = sorted(ratio_mean_dic.items(), key=lambda x: x[1], reverse = True)
    sorted_ratio_median = sorted(ratio_median_dic.items(), key=lambda x: x[1], reverse = True)

    chemical_mean = list(zip(*sorted_ratio_mean))[0]
    chemical_median = list(zip(*sorted_ratio_median))[0]
    ra_mean = list(zip(*sorted_ratio_mean))[1]
    ra_median = list(zip(*sorted_ratio_median))[1]
    x_pos_mean = np.arange(len(chemical_mean))
    x_pos_median = np.arange(len(chemical_median))

    # plt.figure(figsize=(11.69,8.27))
    # plt.bar(x_pos_mean, ra_mean ,align='center', color = '#80B1D3')

    # plt.xticks(x_pos_mean, chemical_mean,rotation=90) 
    # plt.ylabel('Ratio (Mean)',fontweight = 'bold')
    # plt.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    # plt.tight_layout(w_pad = 2, h_pad = 2)
    # plt.savefig('./output3/Seasonal_Ratio_(Mean)_{}_{}.png'.format(location, now.strftime("%Y-%m-%d_%H-%M")))

    plt.figure(figsize=(11.69,8.27))
    barlist = plt.bar(x_pos_median, ra_median ,align='center', color = '#80B1D3')
    for i in range(1,13):
        barlist[-i].set_color('#EA8E83')
    plt.xticks(x_pos_median, chemical_median, rotation=90) 
    plt.ylabel('Ratio (Median)',fontweight = 'bold')
    plt.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    plt.tight_layout(w_pad = 2, h_pad = 2)
    plt.savefig('./output3/Seasonal_Ratio_(Median)_{}_{}.png'.format(location, now.strftime("%Y-%m-%d_%H-%M")))

def plot_rush_ratio(location):
    rush_hour_ratio = rush_hour(main_df,chem_names)
    sorted_rush = sorted(rush_hour_ratio.items(), key=lambda x: x[1], reverse = True)

    chemical = list(zip(*sorted_rush))[0]
    ra = list(zip(*sorted_rush))[1]
    x_pos = np.arange(len(chemical))

    plt.figure(figsize=(11.69,8.27))
    barlist = plt.bar(x_pos, ra,align='center', color = '#80B1D3')
    barlist[0].set_color('#EA8E83')
    barlist[1].set_color('#EA8E83')
    barlist[2].set_color('#EA8E83')
    barlist[3].set_color('#EA8E83')
    barlist[4].set_color('#EA8E83')
    plt.xticks(x_pos, chemical,rotation=90) 
    plt.ylabel('Ratio (Mean)',fontsize = 12, fontweight = 'bold',labelpad = 4)
    plt.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    plt.tight_layout(w_pad = 2, h_pad = 2)
    plt.savefig('./output3/Weekday_Ratio_{}_{}.png'.format(location, now.strftime("%Y-%m-%d_%H-%M")))


location = 'YL'

t = get_chemicals(location)
chem_df = t[0]
count_lol = t[1]
count_inval = t[2]
wind_df = get_wind()


if location == 'YL':
        main_df = merge_dataframe(chem_df,wind_df)

if location == 'MK':
        main_df = chem_df


main_df.fillna(value=pd.np.nan, inplace=True)

chem_names = chem_names()
print(chem_names)

day_of_week = []
time_of_day = []
month = []

for index in main_df.index:
    time_of_day.append(index.time())
    month.append(index.month)

    if index.weekday() > 5:
        day_of_week.append('Holiday')
    else:
        day_of_week.append('Weekday')  


holiday_list = get_holiday(location)


for i in holiday_list:
    day_of_week[i] = 'Holiday'


# main_df now has weekday column and time_of_day column
main_df['day_of_week'] = day_of_week
main_df['time_of_day'] = time_of_day
main_df['month'] = month

# df with only summer rows
summer_df = main_df['2011-5-16':'2011-9-15']  

# df with only winter rows
winter_df = main_df['2011-11-16':'2012-03-15']


# find invalid data
invalid_list = []
for chem in chem_names:
    if summer_df[chem].count() < 1476 or winter_df[chem].count() < 1452:
        invalid_list.append(chem)


# clear rows with no wind data. For YL only
if location == 'YL':
    rose_df = main_df
    rose_df['ErrFlag'].fillna(-99999.0, inplace=True)
    rose_df = rose_df[rose_df['ErrFlag'] == 0] 



now = datetime.now()

# plotting graphs
plot_all(location)


# # get summer/winter ratio
# plot_seasonal_ratio(location)

# rush_hour_ratio = rush_hour(main_df,chem_names)
# plot_rush_ratio(location)

# stats = main_df.describe()
# stats.to_csv('hey',sep='\t')

# get correlations
# correlation(main_df, 'n-butane', 'i-butane',location)
# correlation(main_df, 'n-pentane', 'i-pentane',location)
# correlation(main_df, 'toluene', 'benzene',location)
# correlation(main_df, 'm-xylene + p-xylene', 'ethylbenzene',location)


# get_mixing_ratio()
# get_ofh()
# get_mir()

# main_df = main_df['2011-5-16':'2011-9-24']
# if location == 'YL':
#         for chemical in ['Ethane','Ethyne', 'n-hexane','benzene']:   
            
#             ttldiurfig = ttl_diur(chemical, location) 
#             plt.savefig('./output{}/{}1_ttl_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M")))
            
                
# if location == 'MK':
#     for chemical in ['Ethane','Ethyne', 'n-hexane','benzene']:   
#         ttldiurfig = ttl_diur(chemical, location) 
#         plt.savefig('./output{}/{}1_ttl_{}.png'.format(location,chemical,now.strftime("%Y-%m-%d_%H-%M"))) 
