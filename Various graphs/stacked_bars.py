import matplotlib.pyplot as plt
import pandas as pd

#Stacked Bars

df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"]
alb_data = df[df.country=="Albania"]
egp_data = df[df.country=="Egypt"]

plt.bar(usa_data.year, usa_data.lifeExp, color ='maroon', width = 0.8, label = "USA")
plt.bar(alb_data.year, alb_data.lifeExp, bottom=usa_data.lifeExp, color ='orange', width = 0.8, label = "Albania")
plt.bar(egp_data.year, egp_data.lifeExp, bottom=alb_data.lifeExp, color ='blue', width = 0.8, label = "Egypt")


plt.legend()
plt.show()


