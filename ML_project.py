import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
df=pd.read_csv("customer_retail csv file.csv")
df=df.dropna()
print(df.head())

df=df[['Quantity','UnitPrice','Country']]
encoder=LabelEncoder()
df['Country_encoded']=encoder.fit_transform(df['Country'])
plt.figure(figsize=(8,5))
plt.scatter(df['Quantity'],df['UnitPrice'])
plt.xlabel('Quantity')
plt.ylabel('UnitPrice')
plt.title('Scatter Plot of Quantity vs UnitPrice')
plt.show()

encoder=LabelEncoder()
df['Country_encoded']=encoder.fit_transform(df['Country'])

x=df[['Quantity','UnitPrice']]
y=df['Country_encoded']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print("Logistic Regression")
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy_logistic=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy_logistic)
print("Confusion Matrix:")
print(confusion_matrix(y_test,y_pred))

print("Decision Tree")
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy_decision=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy_decision)
print("Confusion Matrix :")
print(confusion_matrix(y_test,y_pred))

print("KNN")
model=KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy_knn=accuracy_score(y_test,y_pred)
print("Accuracy:",accuracy_knn)
print("Confusion Matrix :")
print(confusion_matrix(y_test,y_pred))

models=[
'Logistic Regression',
'Decision Tree',
'KNN']
accuracies=[
    accuracy_logistic,
    accuracy_decision,
    accuracy_knn
]
plt.figure(figsize=(8,5))
plt.bar(models,accuracies)
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()