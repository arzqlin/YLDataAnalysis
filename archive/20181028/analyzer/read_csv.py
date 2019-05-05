import csv
import pandas as pd

with open('/Users/ChloeLam/Desktop/ChemProject/2011VOC/wind_data/wind_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0

    
    for row in csv_reader:
        if line_count < 6:
            line_count += 1
        else:
            print(row[0],row[1],row[2],row[3],row[4])
            line_count += 1
    print('Processed {} lines.'.format(line_count))


class Wind:
    def __init__(self, day, time):
        self.day = day
        self.time = time
    