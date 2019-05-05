from analyzer.mean_pct import data_avg, find_percentile

def diur(input_data, day_map): 
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    time_list = []

    for chem_index in range(30):
        time_list.append([])
        
        for i in range(48) :
            time_list[chem_index].append([])

        for i in range(12):
            for j in range(days_in_months[i]):
                if day_map()[i][j] == True:
                    data = input_data[chem_index].get_date(i,j)
                    for time in range(48):
                        time_list[chem_index][time].append(data[time])
    
    return time_list

#get diurnal averaged data 
def diur_average(input_data, day_map):
    time_list = diur(input_data, day_map)

    avg_time_list = []

    for chem_index in range(30):
        avg_time_list.append([])
        for time in range(48):
            avg = data_avg(time_list[chem_index][time])
            avg_time_list[chem_index].append(avg)

    return avg_time_list

#get diurnal percentile data, specifically :  25%, median, 75%
def diur_percentile(input_data, day_map,percentile):
    time_list = diur(input_data, day_map)

    percentile_time_list = []
    
    for chem_index in range(30):
        percentile_time_list .append([])
        for time in range(48):
            percent = find_percentile(time_list[chem_index][time], percentile)
            percentile_time_list[chem_index].append(percent)

    return percentile_time_list