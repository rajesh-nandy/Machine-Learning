import plotly.express as px
import pandas as pd
#Gantt Chart
df = pd.read_csv("population.csv")
eu_data = df[df.continent=="Europe"]
eu_data = eu_data[(eu_data.year == 2007) | (eu_data.year == 1987)].head(20)

fig = px.timeline(eu_data, x_start="pop", x_end="gdpPercap", y="country", color="year")
fig.update_yaxes(autorange="reversed")
fig.show()
