import json
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
import xlrd
import numpy as np


class Analyzer:
    def __init__(self):

    def get_data(self, month, chemical, day, half_hour):
        return self.months[month][chemical][day][half_hour]

    def get_chemicals(self):
        book = xlrd.open_workbook('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-01.xls')
        chemicals = []

        for i in range(1, book.nsheets):
            chemicals.append(book.sheet_by_index(i).name)

        return chemicals

    def chemical_monthly_sum(self, chemical, month, mask=None):
        sum = [0] * 48
        days = [0] * 48

        for i in range(len(self.months[month][chemical])):
            if not mask or (mask and i < len(mask) and mask[i]):
                daily = self.months[month][chemical][i]

                for j in range(48):
                    if daily[j]:
                        days[j] += 1
                        sum[j] += daily[j]

        # if month == 0:
        #     print(mask)
        #     print(days)
        return (sum, days)

        self.weekdays_map = []
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(12):
            day = sum(days_in_months[:i])
            self.weekdays_map.append([])

            for j in range(days_in_months[i]):
                if day % 7 == 0 or day % 7 == 1:
                    self.weekdays_map[-1].append(False)
                else:
                    self.weekdays_map[-1].append(True)

                day += 1

    def yearly_weekday_avg(self, chemical, weekdays=True, weekends=True, holidays=True):
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        sum = [0] * 48
        days = [0] * 48
        mask = []

        for i in range(12):
            mask.append([False] * days_in_months[i])

            if weekdays:
                mask[i] = [a or b for a, b in zip(self.weekdays_map[i], mask[i])]

            if weekends:
                mask[i] = [not a or b for a, b in zip(self.weekdays_map[i], mask[i])]

            if holidays:
                mask[i] = [a or b for a, b in zip(self.holidays_map[i], mask[i])]
            else:
                mask[i] = [not a and b for a, b in zip(self.holidays_map[i], mask[i])]

            monthly_sum, days_in_month = self.chemical_monthly_sum(chemical, i, mask=mask[i])
            days = [a + b for a, b in zip(days, days_in_month)]
            sum = [a + b for a, b in zip(sum, monthly_sum)]

        return [a / b if b else None for a,b in zip(sum, days)]

    def read_files(self):
        self.months = []
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-01.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-02.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-03.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-04.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-05.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-06.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-07.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-08.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-09.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-10.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-11.xls'))
        self.months.append(self.read_file('/User/ChloeLam/Desktop/ChemProject/2011VOC/YL real-time VOC 2011-12.xls'))

    def read_file(self, filepath):
        month = {}
        book = xlrd.open_workbook(filepath)

        for i in range(1, book.nsheets):
            sh = book.sheet_by_index(i)
            month[sh.name] = []

            for j in range(1, sh.ncols, 2):
                day = self.parse_data(sh.col_values(j)[4:52])
                month[sh.name].append(day)

        return month

    def parse_data(self, array):
        for i, element in enumerate(array):
            if '<' in str(element):
                array[i] = 0
            elif '****' in str(element):
                array[i] = None

        return array

    def plot_graph(num_of_graph, xa, inv, fig_size,ya, x_label, folder_loc, pic_name):
        for i in range(num_of_graph):
            t = np.arange(1, xa, inv)
            plt.figure(figsize = fig_size, dpi=100)
            plt.plot(t, ya[i])
            plt.yticks(np.arange(0, max(x for x in ya[i] if x is not None) + 1, 1.0))
            plt.ylabel(chemical_name[i] + '  Concentration (ppbv)')
            plt.xlabel('%s' % (x_label))
            plt.savefig('/Users/ChloeLam/Desktop/Chem MSc Project/' + '%s' % (folder_loc) + '/2011_' + chemical_name[i] + '_' +  '%s' % (pic_name) + '.png')


def main():
    analyzer = Analyzer()

    # weekdays_avg = analyzer.yearly_weekday_avg('i-butane', weekdays=True, weekends=False, holidays=False)
    # holidays_avg = analyzer.yearly_weekday_avg('i-butane', weekdays=False, weekends=True, holidays=True)
    # x = np.arange(1,25,1/2)
    # plt.plot(x, weekdays_avg)
    # plt.plot(x, holidays_avg)
    # plt.legend(['weekdays', 'weekend + holidays'], loc='upper left')
    # plt.savefig('/Users/ChloeLam/Desktop/Chem MSc Project/2011VOC/Diur_Weekday_Holiday/' + 'i-butane' + '.png')

    fig, ax = plt.subplots()

    for chemical in analyzer.get_chemicals():
        weekdays_avg = analyzer.yearly_weekday_avg(chemical, weekdays=True, weekends=False, holidays=False)
        holidays_avg = analyzer.yearly_weekday_avg(chemical, weekdays=False, weekends=True, holidays=True)
        plt.figure(figsize=(8, 10), dpi=100)
        x = np.arange(1,25,1/2)
        plt.plot(x, weekdays_avg)
        plt.plot(x, holidays_avg)
        plt.legend(['weekdays', 'weekend + holidays'], loc='upper left')
        plt.ylabel(chemical + '  Concentration (ppbv)')
        plt.xlabel('Diurnal Variation (Yearly Average)')
        plt.savefig('/Users/ChloeLam/Desktop/Chem MSc Project/2011VOC/Diur_Weekday_Holiday/' + chemical + '.png')
        plt.cla()
    plt.close(fig)

if __name__ == '__main__':
    main()
