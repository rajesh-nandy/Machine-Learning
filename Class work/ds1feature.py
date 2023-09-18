import numpy as np
import pandas as pd



df = pd.read_csv("world_population.csv")
feature = [" Population", "Area (km²)", "Density (per km²)", "Growth Rate", "World Population Percentage"]
for k in feature:
    if k == " Population":
        year = [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]
        for i in year:
            s = str(i) + k
            print(" Median, Mean, Mode and Standard Deviation for " + s)
            print(df[s].median())
            print(df[s].mean())
            print(df[s].mode())
            print(df[s].std())

    else:
        print(" Median, Mean, Mode and Standard Deviation for " + k)
        print(df[k].median())
        print(df[k].mean())
        print(df[k].mode())
        print(df[k].std())
    
print("Countries count by Continent: \n ", df[['Continent', 'Country/Territory']].groupby('Continent').count())
ranking_bins = pd.IntervalIndex.from_tuples([(0, 40), (40, 80), (80, 100), (100, 140), (140, 180), (180, 240)])
df['Ranking Range'] = pd.cut(df['Rank'], bins=ranking_bins)

print("Countries under various Ranking Catagories: \n ", df[['Ranking Range', 'Country/Territory']].groupby('Ranking Range').count())





