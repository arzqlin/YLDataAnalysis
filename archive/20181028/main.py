import json
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
from analyzer import chemical,read_files,mean_pct,sprweekday
import xlrd
import numpy as np
import itertools
from analyzer.chemical import Chemical
from analyzer.diur_process import diur, diur_average, diur_percentile
from analyzer.mean_pct import data_avg, find_percentile
from analyzer.sd_sem import sd, sem
from analyzer.read_files import read_files
from analyzer.sprweekday import get_holidays, get_weekdays, get_saturdays
from analyzer.del_spikes import del_spikes
from draw_graph.boxplot import boxplot

import plotly
plotly.tools.set_credentials_file(username='arzqlin', api_key='YoTKTkkDYo3A8PyC8AdV')


days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# get a list of chemical names
book = xlrd.open_workbook('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-01.xls')
chem_names = []

for i in range(1, book.nsheets):
    chem_names.append(book.sheet_by_index(i).name)


# create a list of class objects called chemicals
chemicals = []

for i in range(30):
    chemicals.append(Chemical(chem_names[i]))


# get data from Excel

read_files(chemicals)
print(chemicals[0])
n_chemicals = del_spikes(chemicals)





#get weekday 24hr averaged data 
# is diur_average(chemicals, get_weekdays)[i] for chemical number i 
for i in range(30):
    l.append(diur_average(chemicals, get_weekdays)[i])

boxplot(l)


#get weekday 24hr data of x percentile
# is diur_percentile(chemicals, get_weekdays, percentile)[i] for chemical number i 

#get weekday 24hr SD and SEM
# is sd(diur(chemicals, get_weekdays)[i]) and  sem(diur(chemicals, get_weekdays)[i])    for chemical number i 



# for i in range(30):
#     print("chemical " , i, " average = ", diur_average(chemicals, get_weekdays)[i])
#     print("chemical " , i, " 95% = ", diur_percentile(chemicals, get_weekdays, 95)[i])
#     print("chemical " , i, " 75% = ", diur_percentile(chemicals, get_weekdays, 75)[i])
#     print("chemical " , i, " 50% = ", diur_percentile(chemicals, get_weekdays, 50)[i])
#     print("chemical " , i, " 25% = ", diur_percentile(chemicals, get_weekdays, 25)[i])
#     print("chemical " , i, " 5% = ", diur_percentile(chemicals, get_weekdays, 5)[i])





#get holiday 24hr averaged data 
# is diur_average(chemicals, get_holidays)[i] for chemical number i 

#get holiday 24hr data of x percentile
# is diur_percentile(chemicals, get_holidays, percentile)[i] for chemical number i 




#get saturday 24hr averaged data 
# is diur_average(chemicals, get_saturdays)[i] for chemical number i 

#get saturday 24hr data of x percentile
# is diur_percentile(chemicals, get_saturdays, percentile)[i] for chemical number i 


