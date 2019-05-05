import xlrd
import numpy as np
import pandas as pd
from datetime import datetime 
from .del_spikes import del_spikes
from .get_detect_lim import get_detect_lim

def chem_names():
    book = xlrd.open_workbook('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-05.xls')
    chem_names = []
    for i in range(1, book.nsheets):
        chem_names.append(book.sheet_by_index(i).name)

    return chem_names

def get_xls(location):
    book = xlrd.open_workbook('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-04.xls')

    chem_dic = {}
    for i in range(1, book.nsheets):
        chem_dic[book.sheet_by_index(i).name] = []

    if location == 'YL':
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-04.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-05.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-06.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-07.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-08.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-09.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-10.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-11.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-12.xls',chem_dic)

        read_file('/Users/ChloeLam/Desktop/ChemProject/2012VOC/YL_real-time_VOC_2012-01.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2012VOC/YL_real-time_VOC_2012-02.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2012VOC/YL_real-time_VOC_2012-03.xls',chem_dic)
    
    if location == 'MK':
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-04.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-05.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-06.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-07.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-08.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-09.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-10.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-11.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC_4_12_MK/MK_real-time_VOC_2011-12.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2012VOC_1_5_MK/MK_real-time_VOC_2012-01.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2012VOC_1_5_MK/MK_real-time_VOC_2012-02.xls',chem_dic)
        read_file('/Users/ChloeLam/Desktop/ChemProject/2012VOC_1_5_MK/MK_real-time_VOC_2012-03.xls',chem_dic)
        
    return chem_dic

def get_time():
    time_half_hour = pd.date_range(start = '4/1/2011', end = '4/1/2012', freq = '0.5H', closed='left')

    return time_half_hour

# Read all the Excel files
def get_chemicals(location):

    chem_dic = get_xls(location)

    # chem_df now has all the data
    chem_df = pd.DataFrame.from_dict(chem_dic, dtype=float)

    time_half_hour = get_time()
    
    chem_df['time'] = time_half_hour

    #set time column as index
    chem_df.set_index('time', inplace = True, drop = True)

    # parse data in df
    lol_dic = get_detect_lim(location)

    count_lol = {}
    count_inval = {}

    for chem in chem_names():        
        t = parse_data(chem_df[chem], chem, lol_dic)
        chem_df.loc[:,chem] = t[0]
        count_lol[chem] = t[1]
        count_inval[chem] = t[2]

    # Attempt to infer better dtypes for object columns.
    chem_df = chem_df.infer_objects()

    # reshape into hourly data
    chem_df = chem_df.resample('H').mean()

    # if the pd.boxplot takes care of the outliers then del_spikes is not needed?
    chem_df = del_spikes(chem_df)

    return chem_df, count_lol, count_inval
    
# Reading a single Excel file
def read_file(filepath, chem_dic):
    
    book = xlrd.open_workbook(filepath)
    
    for i in range(1,book.nsheets):
        
        sh = book.sheet_by_index(i)  # sh is the current sheet being read, 
        sh_name = sh.name

        for j in range(1, sh.ncols, 2):
            
            for k in range(4,52):

                value = sh.cell_value(k,j)

                chem_dic[sh_name].append(value)
                       
# Turn invalid data into None and small data into half the LOL
def parse_data(ts, chem, lol_dic):
    checker_lol = 0
    checker_inval = 0

    for i,v in ts.items():

        month = i.month

        new_value = float(lol_dic[chem][month])

        if v == '< ':
            ts.at[i] = 0.5 * new_value
            checker_lol += 1

        elif v == '****':
            ts.at[i] = None
            checker_inval += 1
            
            
    return ts, checker_lol, checker_inval

if __name__ == '__main__':
    print(lol())

