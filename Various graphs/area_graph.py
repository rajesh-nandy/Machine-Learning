import matplotlib.pyplot as plt
import pandas as pd

#Area Graph

df = pd.read_csv("population.csv")
usa_data = df[df.country=="United States"].to_numpy()
cnd_data = df[df.country=="Canada"].to_numpy()
fig, ax = plt.subplots(figsize=(8, 8))


ax.plot(usa_data[:, 2], usa_data[:, 5], color="green")
ax.plot(cnd_data[:, 2], cnd_data[:, 5], color="red")

print(usa_data[:, 2], usa_data[:, 5], cnd_data[:, 5])
ax.fill_between(
    usa_data[:, 2].astype(int), usa_data[:, 5].astype(int), cnd_data[:, 5].astype(int), where=(usa_data[:, 5].astype(int) < cnd_data[:, 5].astype(int)), 
    interpolate=True, color="green", alpha=0.25
)
ax.fill_between(
    usa_data[:, 2].astype(int), usa_data[:, 5].astype(int), cnd_data[:, 5].astype(int), where=(usa_data[:, 5].astype(int) > cnd_data[:, 5].astype(int)), 
    interpolate=True, color="red", alpha=0.25
)

ax.set_xlabel("Year",color="green",fontsize=14)
ax.set_ylabel("Life expectancy",color="blue",fontsize=14)
plt.show()
