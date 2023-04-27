import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['Date'], dayfirst='false')
df = df.drop(columns=[df.columns[2], df.columns[3]], axis=1)
value = df.columns[1]

df_by_time = df.groupby(df.Date.dt.time)[[value]].median()
df_by_time.plot()

plt.show()