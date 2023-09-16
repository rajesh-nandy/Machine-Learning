import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Scatter Plot

df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"].to_numpy()
cnd_data = df[df.country=="Canada"].to_numpy()

plt.scatter(usa_data[:,2], usa_data[:, 6], c ="pink", linewidths = 2, marker ="s",
            edgecolor ="green",s = 50)
 
plt.scatter(cnd_data[:,2], cnd_data[:,6], c ="yellow", linewidths = 2, marker ="^",
            edgecolor ="red",s = 200)
 
plt.xlabel("Year", color="green",fontsize=14)
plt.ylabel("Yearly GDP", color="blue",fontsize=14)
plt.show()