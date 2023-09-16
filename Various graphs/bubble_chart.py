import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Bubble Chart

df = pd.read_csv("population.csv")
austria_data = df[df.country=="Austria"].to_numpy()
angola_data = df[df.country=="Angola"].to_numpy()

plt.scatter(austria_data[:,2], austria_data[:, 3], c ="pink", linewidths = 2, 
            edgecolor ="green",s = (austria_data[:,6]/100).astype(float))
 
plt.scatter(angola_data[:,2], angola_data[:,3], c ="yellow", linewidths = 2, 
            edgecolor ="red",s = (angola_data[:,6]/100).astype(float))
 
plt.xlabel("Year", color="green",fontsize=14)
plt.ylabel("Yearly GDP", color="blue",fontsize=14)
plt.show()