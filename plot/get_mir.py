import xlrd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from datetime import datetime
import seaborn as sns

def get_mir():
    YL_MIR = {}

    book = xlrd.open_workbook('/Users/ChloeLam/Desktop/ChemProject/Project/comparison.xlsx')
        
    sh = book.sheet_by_index(0)  # sh is the current sheet being read, 
    chem_name = []
    for j in range(1, 30):  
        chem = sh.cell_value(0,j) 
        chem_name.append(chem)      
        YL_MIR[chem] = np.float64(sh.cell_value(20,j))

    sorted_MIR = sorted(YL_MIR.items(), key=lambda x: x[1], reverse = True)

    chemical = list(zip(*sorted_MIR))[0]
    ra = list(zip(*sorted_MIR))[1]
    x_pos = np.arange(len(chemical))

    plt.figure(figsize=(11.69,8.27),dpi = 100)
    barlist = plt.bar(x_pos, ra,align='center', color = '#80B1D3')
    barlist[0].set_color('#EA8E83')
    barlist[1].set_color('#EA8E83')
    barlist[2].set_color('#EA8E83')
    plt.xticks(x_pos, chemical,rotation=90) 
    plt.ylabel('Maximum Incremental Reactivity',fontsize = 12, fontweight = 'bold',labelpad = 4)
    plt.grid(True,color='#404040',alpha = 0.05, linestyle='-',linewidth = 1 )
    plt.tight_layout(w_pad = 2, h_pad = 2)

    now = datetime.now()
    plt.savefig('./output3/MIR_YL_{}.png'.format(now.strftime("%Y-%m-%d_%H-%M")))