import matplotlib.pyplot as plt
import pandas as pd

#Box Plot

df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"].lifeExp
cnd_data = df[df.country=="Canada"].lifeExp
bza_data = df[df.country=="Brazil"].lifeExp
bnd_data = df[df.country=="Bangladesh"].lifeExp


ds = [usa_data, cnd_data, bza_data, bnd_data]
fig = plt.figure(figsize =(10, 7))
plt.boxplot(ds)
 
# show plot
plt.show()