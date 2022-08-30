import datetime
import csv

def save_csv(topic, member):

    date = datetime.datetime.now().strftime('%x')
    time = datetime.datetime.now().strftime('%X')

    with open('C://Users//pc//Desktop//Codes//Group//data.csv','a+',newline='') as f :
        csv_write = csv.writer(f)
        data_row = [date, time, topic, member]
        csv_write.writerow(data_row)

    print(time + ' Success')