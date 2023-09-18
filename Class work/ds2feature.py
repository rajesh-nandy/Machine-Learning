import numpy as np
import pandas as pd


df = pd.read_csv("business.retailsales.csv")
feature = ["Net Quantity", "Gross Sales", "Discounts", "Returns", "Total Net Sales"]
for k in feature:
    print(" Median, Mean, Mode and Standard Deviation for " + k)
    print(df[k].median())
    print(df[k].mean())
    print(df[k].mode())
    print(df[k].std())

print("Product Sales count by Type: \n ", df.groupby('Product Type').sum())


    
