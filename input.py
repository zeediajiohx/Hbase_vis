import happybase
import pandas as pd

connection = happybase.Connection('192.168.56.101')
table=connection.table('populations')

s=pd.read_csv('newpopulation.csv',encoding='gbk')
dataN,paraN=s.shape

for i in range(dataN):
    a=s.iloc[i].values
    year = str(a[0])
    popu='popu:'+a[1]
    rank='rank:'+a[1]
    cont='cont:'+a[1]
    data = {popu:str(a[4]),rank:str(a[3]),cont:a[2]}
    table.put(row=year,data=data)

    print(i,"over")
print("over")
