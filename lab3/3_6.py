import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table 

#fig, ax = plt.subplots()
#
#ax = plt.subplot(111, frame_on=False) 
#ax.axis('off')
#ax.axis('tight')

df1 = pd.DataFrame({  'name':['Александр', 'Сергей', 'Петр', 'Мария', 'Анна'],
                       'age':[         29,       45,     18,      20,     27],
                    'income':[      80000,   150000,  60000,   90000, 100000]})

df2 = pd.DataFrame({ 'name':['Александр', 'Иван', 'Петр', 'Ольга', 'Анна'],
                      'car':[         1,      2,     1,      1,         3],
                    'hobby':['спорт', 'рисование', 'музыка', 'чтение', 'домашние животные']})

newDF = pd.concat([df1,df2], axis=1)

newDF = newDF.loc[:,~newDF.columns.duplicated()].copy()

incomeMean = newDF.groupby(['car']).agg({'income': ['mean']}).reset_index()

print(newDF)
print(incomeMean)

#incomeMean.to_csv(r'C:\Users\GreenDe\Desktop\VUZ\MAI-Labs\lab3\3_6file.txt', header=None, index=None, sep=' ', mode='a')
#incomeMean.to_html(r'C:\Users\GreenDe\Desktop\VUZ\MAI-Labs\lab3\3_6file1.html')

#table(ax, data)  