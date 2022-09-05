import datetime
import csv


def save_csv(fileolc,data1, data2, data3='',data4=''):

    # data3 & data4 optional parameter

    date = datetime.datetime.now().strftime('%x')
    time = datetime.datetime.now().strftime('%X')

    with open(fileolc,'a+',newline='') as f :
        csv_write = csv.writer(f)
        if data3:
            if data4:
                data_row = [date, time[:-3], data1, data2, data3, data4]
            else :
                data_row = [date, time[:-3], data1, data2, data3]
        else:
            data_row = [date, time[:-3], data1, data2]     
                      
        csv_write.writerow(data_row)

    print(time + ' Success')




def last_data(fileloc,n):
    with open(fileloc,'r') as f :
        mLines = f.readlines()
    targetLine = mLines[-1]
    a = targetLine.split(',')[n]
    return a