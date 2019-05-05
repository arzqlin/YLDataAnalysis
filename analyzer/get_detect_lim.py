import xlrd
import numpy as np
import pandas as pd

def get_detect_lim(location):
    if location == 'YL':
        book = xlrd.open_workbook('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_LOL.xls')
    elif location == 'MK':
        book = xlrd.open_workbook('/Users/ChloeLam/Desktop/ChemProject/2012VOC_1_5_MK/MK_real-time_VOC_LOL.xls')

    sh = book.sheet_by_index(0)  # sh is the current sheet being read,
    lol_dic = {}

    month = [4,5,6,7,8,9,10,11,12,1,2,3]

    for i in range(2,32): # each row
        chem_name = sh.cell_value(i,1)  # get chemical name
        lol_dic[chem_name] = {}

        for j in range(2, 14):
            value = sh.cell_value(i,j)

            month_now = month[j-2]

            lol_dic[chem_name][month_now] = value

    return lol_dic

if __name__ == '__main__':
    print(get_detect_lim('YL'))
    

    