import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

pd.to_datetime("10.11.2020")

cols = ["Имя", "Возраст", "Пол", "Дата продажи товара", "Кол-во товара"]
rows = np.array([["Алексей", 25, "муж", pd.to_datetime("10.11.2020"), 2000], 
                ["Иван", 30, "муж", pd.to_datetime("05.12.2019"), 2539],
                ["Андрей", 31, "муж", pd.to_datetime("11.11.2015"), 4000],
                ["Владимир", 43, "муж", pd.to_datetime("25.09.2022"), 715],
                ["Татьяна", 27, "жен", pd.to_datetime("07.08.2021"), 1500]])

df = pd.DataFrame(rows, columns=cols)

ax.table(cellText=df.values, colLabels=df.columns, loc='center')

fig.tight_layout()

plt.show()