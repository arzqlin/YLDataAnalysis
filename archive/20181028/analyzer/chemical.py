import json
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
import xlrd
import numpy as np
from itertools import chain
from collections import defaultdict
from .sprweekday import get_weekdays, get_holidays
from .mean_pct import data_avg, find_percentile

class Chemical:
    def __init__(self, name):
        self.data = []
        self.name = name
    
    def get_time(self, month, date, time):
        return self.data[month][date][time]

    def get_date(self, month,date):
        return self.data[month][date]
    
    def get_month(self, month):
        return self.data[month]
    
    def weekday_data(self):
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        weekday_list = []
        for i in range(12):
            for j in range(days_in_months[i]):
                map = get_weekdays()
                if map[i][j] == True:
                    weekday_list.append(self.get_date(i,j))
        return weekday_list
            


