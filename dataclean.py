import pandas as pd
import math


# 小组增长数据（两个新字段）
loc = 'C://Users//pc//Desktop//Codes//Group//data_new.csv'

reader = pd.read_csv(loc)

for i in range(307):
    reader['Member'].loc[i+1] = reader['Topic_increase'].loc[i+1]
for i in range(307):    
    reader['Topic_increase'].loc[i+1] = reader['Topic'].loc[i+1]-reader['Topic'].loc[i]  
    reader['Member_increase'].loc[i+1] = reader['Member'].loc[i+1]-reader['Member'].loc[i]
    
for i in range(308):
    if(math.isnan(reader['Member'].loc[i])):
        reader['Member'].loc[i] = 999999
    if(math.isnan(reader['Member_increase'].loc[i])):
        reader['Member_increase'].loc[i] = 999999

reader['Member']=reader['Member'].astype(int)
reader['Member_increase']=reader['Member_increase'].astype(int)

reader.to_csv('C://Users//pc//Desktop//Codes//Group//data_new.csv',index=None)

print(reader)








# 话题-时间数据
'''
reader = pd.read_csv('C://Users//pc//Desktop//Codes//Group//onetopic_new.csv')
print(reader.loc[0][1][:-3]) 

for i in range(191):
    reader['time'].loc[i] = reader.loc[i][1][:-3]
    reader['data_increase'].loc[i] = int(reader['data_increase'].loc[i])

reader.to_csv('C://Users//pc//Desktop//Codes//Group//onetopic_new.csv',index=None)

print(reader)
'''

# 小组-时间数据
'''
reader = pd.read_csv('C://Users//pc//Desktop//Codes//Group//data_new.csv')


for i in range(307):
    reader['Time'].loc[i] = reader.loc[i][1][:-3]
#    reader['data_increase'].loc[i] = int(reader['data_increase'].loc[i])

reader.to_csv('C://Users//pc//Desktop//Codes//Group//data_new.csv',index=None)

print(reader)

'''