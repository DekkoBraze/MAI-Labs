import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table 

data = pd.read_csv('stockholm_td_adj.dat.txt', header=None, sep="\s+", names=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(data)
print("Типы столбцов:", data['a'].dtype, data['b'].dtype, data['c'].dtype, data['d'].dtype, data['e'].dtype, data['f'].dtype,
      data['g'].dtype)