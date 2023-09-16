import plotly.express as px
import pandas as pd
#Funnel Chart
df = pd.read_csv("population.csv")
eu_data = df[df.continent=="Europe"]
eu_data = eu_data[eu_data.year == 1982].head(20)
eu_data = eu_data.sort_values(by = "gdpPercap")

fig = px.funnel(eu_data, y='country', x='gdpPercap')
fig.show()