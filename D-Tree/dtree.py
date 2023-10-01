import pandas as pd
import numpy as np 
import tree

import warnings
warnings.filterwarnings('ignore')


col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
             'occupation', 'relationship','race', 'sex', 'capital_gain', 'capital_loss',
              'hours_per_week', 'native_country', 'income']

df = pd.read_csv("adult.csv", names=col_names)

#print(df.head(10))
categorical = [var for var in df.columns if df[var].dtype=='O']
#print(categorical)
  
df['workclass'].replace(' ?', np.NaN, inplace=True)
df['occupation'].replace(' ?', np.NaN, inplace=True)
df['native_country'].replace(' ?', np.NaN, inplace=True)

"""print(df[categorical].isnull().sum())
for i in categorical:    
    print(i, ' contains ', len(df[i].unique()), ' labels')"""



x = df
n = (len(x)//4)*3
x_train, x_test= x[:n], x[n:]
#print(x_test, y_test)

categorical = [col for col in x_train.columns if x_train[col].dtypes == 'O']
numerical = [col for col in x_train.columns if x_train[col].dtypes != 'O']
for data in [x_train,x_test]:
    data['workclass'].fillna(x_train['workclass'].mode()[0],inplace=True)
    data['occupation'].fillna(x_train['occupation'].mode()[0],inplace=True)
    data['native_country'].fillna(x_train['native_country'].mode()[0],inplace=True)

#print(x_test[categorical].isnull().sum())
categorical = ['age', 'workclass', 'marital_status',
             'race', 'sex',]
dt = tree.tree()
dt.grow_tree(x, categorical, 'income')



