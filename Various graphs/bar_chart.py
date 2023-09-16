import matplotlib.pyplot as plt
import pandas as pd

#Bar Chart
df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"]
fig,ax = plt.subplots()




ax.bar(usa_data.year, usa_data.lifeExp, color ='maroon', width = 3)
ax.set_xlabel("Year",color="green",fontsize=14)
ax.set_ylabel("Life expectency",color="blue",fontsize=14)
plt.show()