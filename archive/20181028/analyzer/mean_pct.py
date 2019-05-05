import numpy as np
import itertools
from . import chemical

def data_avg(l):
    # l = [x for x in list(itertools.chain.from_iterable(l)) if x is not None]
    l = [x for x in l if x is not None]
    avg = 1.0 * sum(l)/len(l)

    return avg


def find_percentile(l, percent):
    l = [x for x in l if x is not None]
    l.sort()
    p = np.percentile(l, percent)
    return p

if __name__ == '__main__':
    YLdata = get_data.get_data()
    sum_avg = {}
    win_avg = {}

    for chemical in YLdata.get_chemicals():
        sum_avg[chemical] = data_avg(YLdata.months[5][chemical] + YLdata.months[6][chemical]+ YLdata.months[7][chemical])
        win_avg[chemical] = data_avg(YLdata.months[11][chemical]+ YLdata.months[0][chemical] + YLdata.months[1][chemical])
        print(chemical, '     ', win_avg[chemical]/sum_avg[chemical])
