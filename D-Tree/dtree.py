import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix
from matplotlib import pyplot as plt
import tree
import warnings

warnings.filterwarnings('ignore')

#adding the column names
col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
             'occupation', 'relationship','race', 'sex', 'capital_gain', 'capital_loss',
              'hours_per_week', 'country', 'income']

df = pd.read_csv("adult.csv", names=col_names)


categorical = [var for var in df.columns if df[var].dtype=='O']

#preprocessing of the data

df['workclass'].replace(' ?', np.NaN, inplace=True)
df['occupation'].replace(' ?', np.NaN, inplace=True)
df['country'].replace(' ?', np.NaN, inplace=True)





x = df
n = (len(x)//4)*3
x_train, x_test= x[:n], x[n:]

#Replacing the missing values withe most frequent element

categorical = [col for col in x_train.columns if x_train[col].dtypes == 'O']
numerical = [col for col in x_train.columns if x_train[col].dtypes != 'O']
for data in [x_train,x_test]:
    data['workclass'].fillna(x_train['workclass'].mode()[0],inplace=True)
    data['occupation'].fillna(x_train['occupation'].mode()[0],inplace=True)
    data['country'].fillna(x_train['country'].mode()[0],inplace=True)



count = x_train['income'].value_counts().tolist()
labels = x_train['income'].unique().tolist()
plt.pie(count, labels = labels)
plt.show()



#taking small set of features for training the model:

p = ['marital_status', 'income', 'workclass', 'race', 'sex']
feature_set = ['marital_status', 'workclass', 'race', 'sex']
x_train = x_train[p]
x_test = x_test[p]

dt = tree.tree()
dt.grow_tree(x_train, dt.root, None, feature_set, 'income')

#testing the model
y_train, y_test = x_train['income'], x_test['income']
y_pred = dt.predict_data(x_test)

print(accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot = True)
plt.show()

#visualization
dt.tree_display(dt.root)
dt.tree_visualization()
