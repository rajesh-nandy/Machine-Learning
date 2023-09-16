import matplotlib.pyplot as plt
import pandas as pd

#Cumulative Histogram
n_bins = 25
df = pd.read_csv("population.csv")
yeardata = df[df.year==2007]
fig, ax = plt.subplots()


ax.hist(yeardata.lifeExp, n_bins, density=True, histtype='step',
        cumulative=True, label='Empirical')
ax.set_xlabel("Life expectancy", color = "red")

plt.show()
                