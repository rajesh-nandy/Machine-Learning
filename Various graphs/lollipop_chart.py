import matplotlib.pyplot as plt
import pandas as pd

#Lollipop Chart
df = pd.read_csv("population.csv")
yr07 = df[df.year==2007].tail(15)
fig,ax = plt.subplots()

ax.stem(yr07.country, yr07.gdpPercap)

ax.set_xlabel("Country",color="green",fontsize=14)
ax.set_ylabel("GDP in 2007",color="blue",fontsize=14)

plt.show()