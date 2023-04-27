import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table 

#fig, ax = plt.subplots()
#
#ax = plt.subplot(111, frame_on=False) 
#ax.axis('off')
#ax.axis('tight')

data = pd.read_csv('C:\\Users\\GreenDe\\Desktop\\VUZ\\MAI-Labs\\lab3\\stockholm_td_adj.dat.txt', header=None, sep="\s+", names=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(data)

#table(ax, data)  
#
#plt.show()