def get_holidays():
    holidays_map = []
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(12):
        day = sum(days_in_months[:i])
        holidays_map.append([])

        for j in range(days_in_months[i]):
            if day % 7 == 1:
                holidays_map[-1].append(True)
            else:
                holidays_map[-1].append(False)

            day += 1
            
    holidays_map[0][0] = True
    holidays_map[1][3] = True
    holidays_map[1][4] = True
    holidays_map[3][4] = True
    holidays_map[3][21] = True
    holidays_map[3][24] = True
    holidays_map[4][1] = True
    holidays_map[4][9] = True
    holidays_map[5][5] = True
    holidays_map[6][0] = True
    holidays_map[8][12] = True
    holidays_map[9][0] = True
    holidays_map[9][4] = True
    holidays_map[11][24] = True
    holidays_map[11][25] = True
    holidays_map[11][26] = True

    return holidays_map

def get_weekdays():
    weekdays_map = []
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(12):
        day = sum(days_in_months[:i])
        weekdays_map.append([])

        for j in range(days_in_months[i]):
            if day % 7 == 0 or day % 7 == 1:
                weekdays_map[-1].append(False)
            else:
                weekdays_map[-1].append(True)

            day += 1
    
    # These are public holidays
    weekdays_map[0][0] = False
    weekdays_map[1][3] = False
    weekdays_map[1][4] = False
    weekdays_map[3][4] = False
    weekdays_map[3][21] = False
    weekdays_map[3][24] = False
    weekdays_map[4][1] = False
    weekdays_map[4][9] = False
    weekdays_map[5][5] = False
    weekdays_map[6][0] = False
    weekdays_map[8][12] = False
    weekdays_map[9][0] = False
    weekdays_map[9][4] = False
    weekdays_map[11][24] = False
    weekdays_map[11][25] = False
    weekdays_map[11][26] = False
    
    return weekdays_map

def get_saturdays():    
    sat_map = []
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(12):
        day = sum(days_in_months[:i])
        sat_map.append([])

        for j in range(days_in_months[i]):
            if day % 7 == 0:
                sat_map[-1].append(True)
            else:
                sat_map[-1].append(False)

            day += 1
    
    # These are public holidays
    sat_map[0][0] = False
    sat_map[1][3] = False
    sat_map[1][4] = False
    sat_map[3][4] = False
    sat_map[3][21] = False
    sat_map[3][24] = False
    sat_map[4][1] = False
    sat_map[4][9] = False
    sat_map[5][5] = False
    sat_map[6][0] = False
    sat_map[8][12] = False
    sat_map[9][0] = False
    sat_map[9][4] = False
    sat_map[11][24] = False
    sat_map[11][25] = False
    sat_map[11][26] = False
    
    return sat_map  



