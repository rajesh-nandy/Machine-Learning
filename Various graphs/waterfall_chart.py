import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Waterfall Chart
df = pd.read_csv("population.csv")

eu_data = df[df.continent=="Europe"]
eu_data = eu_data[eu_data.year == 2007].head(10)
eu_data['gdp_tot']= eu_data["gdpPercap"].cumsum()
eu_data['gdp_tot2']= eu_data["gdp_tot"].shift(1).fillna(0)
lower = eu_data[['gdp_tot','gdp_tot2']].min(axis=1)
upper = eu_data[['gdp_tot','gdp_tot2']].max(axis=1)
print(eu_data)
fig,ax = plt.subplots()
ax.bar(x=eu_data['country'],height=upper,)
ax.bar(x=eu_data['country'], height=lower,color='white')

plt.show()