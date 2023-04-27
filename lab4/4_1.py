import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(r'C:\Users\GreenDe\Desktop\VUZ\MAI-Labs\lab4\Fremont_Bridge_Bicycle_Counter.csv')

print('Кол-во строк:', len(df))
print('Кол-во столбцов:', len(df.columns))

#Столбцы
#1. Время
#2. Всего прогулок = 3. + 4.
#3. Прогулок на восточной части
#4. Прогулок на западной части

df['Date'] = pd.to_datetime(df['Date'], dayfirst='false')
df = df.drop(columns=[df.columns[2], df.columns[3]], axis=1)

print(df)