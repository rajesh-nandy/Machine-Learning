import matplotlib.pyplot as plt
import pandas as pd

#Dual Cobination Chart
df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"]


fig,ax = plt.subplots()

ax.bar(usa_data.year, usa_data.gdpPercap, color="cyan", width = 3)
# set x-axis label
ax.set_xlabel("year", fontsize = 14, color="green")
# set y-axis label
ax.set_ylabel("gdpPercap", color="red", fontsize=14)


ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(usa_data.year, usa_data.lifeExp,color="red")
ax2.set_ylabel("lifeExp",color="blue",fontsize=14)
plt.show()