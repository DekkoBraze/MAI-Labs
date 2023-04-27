import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

#url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
#df = pd.read_csv(url)
df = pd.read_csv(r'C:\Users\GreenDe\Desktop\VUZ\MAI-Labs\lab4\Fremont_Bridge_Bicycle_Counter.csv')

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

coord = np.array(coord)

gaus = GaussianMixture(n_components=7)
gaus.fit(coord)
ids = gaus.predict(coord)

plt.scatter(x, y, c=ids, s=15, cmap='viridis')

#plt.scatter(x, y)
plt.show()
