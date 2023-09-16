import matplotlib.pyplot as plt
import pandas as pd

#Histogram

df = pd.read_csv("population.csv")
yeardata = df[df.year==2007]
fig, ax = plt.subplots()
ax.hist(yeardata.lifeExp, bins = [*range(40,90,2)])
ax.set_xlabel("Life expectancy", color = "red")
 
plt.show()