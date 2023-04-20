import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

data = pd.read_csv('C:\\Users\\GreenDe\\Desktop\\VUZ\\Proga (labs)\\lab3\\stockholm_td_adj.dat.txt', header=None, sep=" ")
print(data)

#df = pd.DataFrame(rows, columns=cols)
#
#ax.table(cellText=df.values, colLabels=df.columns, loc='center')
#
#fig.tight_layout()
#
#plt.show()