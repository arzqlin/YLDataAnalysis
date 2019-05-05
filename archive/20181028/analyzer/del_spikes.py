import numpy
from .mean_pct import data_avg
from .sd_sem import sd
from .chemical import Chemical


def numpy_flat(a):
    return list(numpy.array(a).flat)

def del_spikes(class_list):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(30):
        flatten=[]
        for m in range(12):
            for d in range(days_in_months[m]):
                for t in range(48):
                    flatten.append(class_list[i].data[m][d][t])


        overall_avg = data_avg(flatten)
        overall_sd = sd(flatten)

        for m in range(12):
            for d in range(days_in_months[m]):
                for t in range(48):
                    if class_list[i].data[m][d][t] is not None:
                        if (class_list[i].data[m][d][t] - overall_avg) > 3 * overall_sd or (class_list[i].data[m][d][t] - overall_avg) < - 3 * overall_sd:
                            if t == 0:
                                if class_list[i].data[m][d-1][-1] == None or class_list[i].data[m][d][1] == None:
                                    class_list[i].data[m][d][t] = None
                                else:
                                    class_list[i].data[m][d][t] = (class_list[i].data[m][d-1][-1] + class_list[i].data[m][d][1])/2
                            elif t == 47:
                                if d == days_in_months[m] - 1:
                                    if class_list[i].data[m][d][46] == None or class_list[i].data[m+1][0][0] == None:
                                        class_list[i].data[m][d][t] = None
                                    else:
                                        class_list[i].data[m][d][t] = (class_list[i].data[m][d][46] + class_list[i].data[m+1][0][0])/2
                                else:
                                    if class_list[i].data[m][d][46] == None or class_list[i].data[m][d + 1][0] == None:
                                        class_list[i].data[m][d][t] = None
                                    else:
                                        class_list[i].data[m][d][t] = (class_list[i].data[m][d][46] + class_list[i].data[m][d + 1][0])/2
                            else: 
                                if class_list[i].data[m][d][t + 1] == None or class_list[i].data[m][d][t - 1] == None:
                                    class_list[i].data[m][d][t] = None
                                else:
                                    class_list[i].data[m][d][t] = (class_list[i].data[m][d][t+1] + class_list[i].data[m][d][t-1])/2

    return class_list