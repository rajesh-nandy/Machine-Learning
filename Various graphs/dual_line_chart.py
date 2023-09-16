import matplotlib.pyplot as plt
import pandas as pd

#Dual Lines Chart
df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"]


fig,ax = plt.subplots()

ax.plot(usa_data.year, usa_data.lifeExp, color="red", marker="o")
# set x-axis label
ax.set_xlabel("year", fontsize = 14)
# set y-axis label
ax.set_ylabel("lifeExp", color="red", fontsize=14)


ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(usa_data.year, usa_data["gdpPercap"],color="blue",marker="o")
ax2.set_ylabel("gdpPercap",color="blue",fontsize=14)
plt.show()