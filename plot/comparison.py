import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from datetime import datetime
import seaborn as sns

def comparison():
    MK_median = {}
    YL_median = {}
    MK_max = {}
    YL_max = {}

    book = xlrd.open_workbook('/Users/ChloeLam/Desktop/ChemProject/Project/comparison.xlsx')
    
    sh = book.sheet_by_index(0)  # sh is the current sheet being read, 
    chem_name = []
    for j in range(1, 30):  
        chem = sh.cell_value(0,j) 
        chem_name.append(chem)      
        MK_median[chem] = np.float64(sh.cell_value(6,j)),'MK'
        YL_median[chem] = np.float64(sh.cell_value(17,j)),'YL'
        MK_max[chem] = np.float64(sh.cell_value(8,j)),'MK'
        YL_max[chem] = np.float64(sh.cell_value(19,j)),'YL'
    
    plot_dic(MK_median,YL_median,'Median',chem_name)
    plot_dic(MK_max,YL_max,'Max',chem_name)
 
def plot_dic(dic1,dic2,label,chem_name):
    now = datetime.now()
    df = pd.DataFrame.from_dict(dic1,orient='index', columns = ['data','location'])
    df1 = pd.DataFrame.from_dict(dic2,orient='index', columns = ['data','location'])

    df = df.append(df1)
    df = df.reset_index()

    df = df.sort_values(by='data', ascending=False)

    chemical = chem_name
    x_pos = np.arange(len(chemical))

    plt.figure(figsize=(11.69,8.27))

    sns.barplot(x = 'index', y = 'data', hue = 'location', palette = 'Set2', data = df,linewidth = 0.8)
    
    plt.xticks(x_pos, chemical,rotation=90)
    plt.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    plt.ylabel('Concentration (ppbv)',fontsize = 12, fontweight = 'bold',labelpad = 4)
    plt.xlabel('',fontsize = 1, fontweight = 'bold',labelpad = 4)
    plt.tight_layout(w_pad = 2, h_pad = 2)
    plt.savefig('../output3/{}_{}.png'.format(label,now.strftime("%Y-%m-%d_%H-%M")))

if __name__ == '__main__':
    comparison()