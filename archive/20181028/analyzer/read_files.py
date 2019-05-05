import json
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
import xlrd
import numpy as np
from itertools import chain
from collections import defaultdict


from .chemical import Chemical


# Read all the Excel files
def read_files(class_list):
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-01.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-02.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-03.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-04.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-05.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-06.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-07.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-08.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-09.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-10.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-11.xls',class_list)
    read_file('/Users/ChloeLam/Desktop/ChemProject/2011VOC/YL_real-time_VOC_2011-12.xls',class_list)


# Reading a single Excel file
def read_file(filepath, class_list):
    
    book = xlrd.open_workbook(filepath)
    

    for i in range(1,book.nsheets):
        sh = book.sheet_by_index(i)
        
        month_data = []
        for j in range(1, sh.ncols, 2):
            day = parse_data(sh.col_values(j)[4:52])
            month_data.append(day)
            
        class_list[i-1].data.append(month_data)
    

# Turn invalid data into None and small data into 0
def parse_data(array):
    for i, element in enumerate(array):
        if '<' in str(element):
            array[i] = 0
        elif '****' in str(element):
            array[i] = None
    return array

if __name__ == '__main__':
    read_files(chemicals)
    print(class_list)