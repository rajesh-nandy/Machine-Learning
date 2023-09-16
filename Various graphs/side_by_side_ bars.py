import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Side-by-Side Bars

df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"]
alb_data = df[df.country=="Albania"]
x_axis= np.arange(len(usa_data.year))


plt.bar(x_axis- 0.2, usa_data.lifeExp, color ='maroon', width = 0.4, label = "USA")
plt.bar(x_axis+ 0.2, alb_data.lifeExp, color ='orange', width = 0.4, label = "Albania")
plt.xticks(x_axis, usa_data.year)

plt.legend()
plt.show()



