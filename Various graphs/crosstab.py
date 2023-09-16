import matplotlib.pyplot as plt
import pandas as pd

#Crosstab with total
def logic(x):
    if x % 12 == 0:
        return False
    else:
        return True
df = pd.read_csv("population.csv", skiprows = lambda x: logic(x))
ct = pd.crosstab(df.country, df.continent, margins=True, margins_name="Total")
print(ct)