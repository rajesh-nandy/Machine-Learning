import matplotlib.pyplot as plt
import squarify 
import pandas as pd
import numpy as np


#Treemap
df = pd.read_csv("population.csv")
yr07 = df[df.year==2007].head(6).to_numpy()
colors = ["red", "black", "green", "violet", "yellow", "blue"]
squarify.plot(sizes=yr07[:,3], color=colors, alpha=0.35)
plt.title("Countries' Population",color="blue",fontsize=14)
plt.show()