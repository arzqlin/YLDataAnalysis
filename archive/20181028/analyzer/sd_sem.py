import statistics
import itertools
import math

#get the standard deviation of a list called l
def sd(l):

    if any(isinstance(i, list) for i in l):
        l = [x for x in list(itertools.chain.from_iterable(l)) if x is not None]
    else:
        l = [x for x in l if x is not None]
    return statistics.stdev(l)

#get the standard error of mean of a list called l
def sem(l):
    
    if any(isinstance(i, list) for i in l):
        l = [x for x in list(itertools.chain.from_iterable(l)) if x is not None]
    else:
        l = [x for x in l if x is not None]
    return statistics.stdev(l)/math.sqrt(len(l))
