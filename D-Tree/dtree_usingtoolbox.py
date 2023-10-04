import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import seaborn as sns
from matplotlib import pyplot as plt


col_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status',
             'occupation', 'relationship','race', 'sex', 'capital_gain', 'capital_loss',
              'hours_per_week', 'country', 'income']

data = pd.read_csv("adult.csv", names=col_names)

data['workclass'].replace(' ?', np.NaN, inplace=True)
data['occupation'].replace(' ?', np.NaN, inplace=True)
data['country'].replace(' ?', np.NaN, inplace=True)

data['workclass'].fillna(data['workclass'].mode()[0],inplace=True)
data['occupation'].fillna(data['occupation'].mode()[0],inplace=True)
data['country'].fillna(data['country'].mode()[0],inplace=True)


wc = data['workclass'].values.reshape(-1,1)
ed = data['education'].values.reshape(-1,1)
ms = data['marital_status'].values.reshape(-1,1)
oc = data['occupation'].values.reshape(-1,1)
rs = data['relationship'].values.reshape(-1,1)
rc = data['race'].values.reshape(-1,1)
sx = data['sex'].values.reshape(-1,1)
nc = data['country'].values.reshape(-1,1)

oe = OrdinalEncoder()

wc_ = oe.fit_transform(wc)
ed_ = oe.fit_transform(ed)
ms_ = oe.fit_transform(ms)
oc_ = oe.fit_transform(oc)
rs_ = oe.fit_transform(rs)
rc_ = oe.fit_transform(rc)
sx_ = oe.fit_transform(sx)
nc_ = oe.fit_transform(nc)

x = np.column_stack((data['age'], wc_, data['fnlwgt'], ed_, data['education_num'], ms_, oc_, rs_, rc_, sx_, data['capital_gain'], data['capital_loss'], data['hours_per_week'], nc_))


le = LabelEncoder()
label = le.fit_transform(data['income'])
data['income'] = label

y = data.iloc[:, -1].values

df = pd.DataFrame(np.hstack((x, y.reshape(-1,1))), columns = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','country','income'])
correlation = df.corr(method = 'pearson')
print(correlation)

plt.figure(figsize = (20,20))
sns.heatmap(correlation, annot = True)
plt.show()
col_names.remove('income')

x = df[col_names].values
y = df['income']

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)

sk_model = DecisionTreeClassifier(max_depth = 4, criterion = 'gini')
sk_model.fit(x_train, y_train)
sk_preds = sk_model.predict(x_test)

print(accuracy_score(y_test, sk_preds))

fig = plt.figure(figsize=(20,20))
_ = tree.plot_tree(sk_model, feature_names=col_names, class_names= ['<=50k','>50k'], filled=True)
plt.show()