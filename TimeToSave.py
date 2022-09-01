import datetime
import csv


def save_csv(topic, member, fileolc):

    date = datetime.datetime.now().strftime('%x')
    time = datetime.datetime.now().strftime('%X')

    with open(fileolc,'a+',newline='') as f :
        csv_write = csv.writer(f)
        data_row = [date, time, topic, member]
        csv_write.writerow(data_row)

    print(time + ' Success')

def last_data(fileloc,n):
    with open(fileloc,'r') as f :
        mLines = f.readlines()
    targetLine = mLines[-1]
    a = targetLine.split(',')[n]
    return a