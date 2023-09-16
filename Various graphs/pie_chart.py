import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Pie Chart

df = pd.read_csv("population.csv")
year2007 = df[df.year==2007].tail(10).to_numpy()
print(year2007[:, 3])
plt.pie(year2007[:,3], labels = year2007[:,1])
plt.show()