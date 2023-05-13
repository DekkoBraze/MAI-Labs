import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table 

df1 = pd.DataFrame({  'name':['Александр', 'Сергей', 'Петр', 'Мария', 'Анна'],
                       'age':[         29,       45,     18,      20,     27],
                    'income':[      80000,   150000,  60000,   90000, 100000]})

df2 = pd.DataFrame({ 'name':['Александр', 'Иван', 'Петр', 'Ольга', 'Анна'],
                      'car':[         1,      2,     1,      1,         3],
                    'hobby':['спорт', 'рисование', 'музыка', 'чтение', 'домашние животные']})

newDF = pd.concat([df1,df2], axis=1)

# loc - формирует новый объект из указанных строк и столбцов
# В данном случае - датафрейм, из которого исключены все дубликаты
# Символ ~ нужен для того, чтобы взять все столбцы, кроме запрошенных в методе duplicated()
# Символ : - это пустой срез (мы берем все строки)
newDF = newDF.loc[:, ~newDF.columns.duplicated()]

# agg - это метод, который позволяет выполнять операции по определенной части датафрейма
# В данном случае мы указываем, что операция mean совершается на колонке income с групировкой записей датафрейма по значению car
incomeMean = newDF.groupby(['car']).agg({'income': ['mean']}).reset_index() # Объяснить

print(newDF)
print(incomeMean)
