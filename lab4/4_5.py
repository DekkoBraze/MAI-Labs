import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)
#df = pd.read_csv(r'C:\Users\GreenDe\Desktop\VUZ\MAI-Labs\lab4\Fremont_Bridge_Bicycle_Counter.csv')

df['Date'] = pd.to_datetime(df['Date'], dayfirst='false')
df = df.drop(columns=[df.columns[2], df.columns[3]], axis=1)
value = df.columns[1]

date_list = df['Date'].dt.date.to_list()
date_list = list(set(date_list))
date_list.sort()
time_list = list(range(24))
table = pd.DataFrame(columns=date_list, index=time_list)
for i in range(len(df['Date'])):
    table[df['Date'][i].date()][df['Date'][i].time().hour] = df[value][i]
table.fillna(0, inplace=True)

pca = PCA(n_components=2)
pca.fit(table)
comp = pca.components_
x = comp[0]
y = comp[1]

coord = []

for a, b in zip(x, y):
    coord.append([a, b])

#Кол-во кластеров
n = 7
coord = np.array(coord)
gaus = GaussianMixture(n_components=n)
gaus.fit(coord)
ids = gaus.predict(coord)

# Как я понял, в ids каждой точке присваивается индекс, который потом раскрашивает cmap
plt.scatter(x, y, c=ids, s=15, cmap='viridis')

#mon = [] #mod = 5
#tue = [] #mod = 6
#wed = [] #mod = 0
#thu = [] #mod = 1
#fri = [] #mod = 2
#sat = [] #mod = 3
#sun = [] #mod = 4
#week = [wed, thu, fri, sat, sun, mon, tue]
#
##Первый день - среда
#for i in range(len(table.columns)):
#    mod = i % 7
#    week[mod].append(ids[i])
#
#print('Monday:')
#for i in range(n):
#    print(i, '=', mon.count(i))

# Кластеризация происходит по удаленности центров точек друг от друга
# В данном случае можно найти кластеризацию по годам

cols = table.columns

years = {2012:[], 2013:[], 2014:[], 2015:[], 2016:[], 2017:[], 2018:[], 2019:[],
         2020:[], 2021:[],2022:[], 2023:[]}

for i in range(len(table.columns)):
    y = table.columns[i].year
    years[y].append(ids[i])

for year in years:
    lst = []
    for i in range(n):
        lst.append(years[year].count(i))
    print(year, '=', lst.index(max(lst)))

plt.show()
# upd