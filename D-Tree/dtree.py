import pandas as pd
import numpy as np 
import tree


import warnings
warnings.filterwarnings('ignore')


col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
             'occupation', 'relationship','race', 'sex', 'capital_gain', 'capital_loss',
              'hours_per_week', 'country', 'income']

df = pd.read_csv("adult.csv", names=col_names)

#print(df.head(10))
categorical = [var for var in df.columns if df[var].dtype=='O']
#print(categorical)
  
df['workclass'].replace(' ?', np.NaN, inplace=True)
df['occupation'].replace(' ?', np.NaN, inplace=True)
df['country'].replace(' ?', np.NaN, inplace=True)

#print(df[categorical].isnull().sum())



x = df
n = (len(x)//4)*3
x_train, x_test= x[:n], x[n:]
#print(x_test, y_test)

categorical = [col for col in x_train.columns if x_train[col].dtypes == 'O']
numerical = [col for col in x_train.columns if x_train[col].dtypes != 'O']
for data in [x_train,x_test]:
    data['workclass'].fillna(x_train['workclass'].mode()[0],inplace=True)
    data['occupation'].fillna(x_train['occupation'].mode()[0],inplace=True)
    data['country'].fillna(x_train['country'].mode()[0],inplace=True)


"""print(x_test[categorical].isnull().sum())
for i in categorical:    
    print(i, ' contains ', len(df[i].unique()), ' labels')

exit(1)"""

p = ['marital_status', 'workclass', 'age', 
             'race', 'sex','income']
feature_set = ['age','marital_status', 'workclass',  
             'race', 'sex',]
x_train = x_train[p]
dt = tree.tree()
dt.grow_tree(x_train, dt.root, None, feature_set, 'income')



