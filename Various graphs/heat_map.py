import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Heat Map

df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"]
cnd_data = df[df.country=="Canada"]
"""data = np.random.random((12, 12))
plt.imshow(usa_data[:,2].astype(int), cmap='autumn', interpolation='nearest')
 
# Add colorbar
plt.colorbar()
 
plt.title("Heatmap with color bar")
plt.show()"""

df = pd.DataFrame(np.random.random((5,5)), columns=["a","b","c","d","e"])
print(df, usa_data)