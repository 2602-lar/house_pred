import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.metrics import mean_absolute_error, accuracy_score



data_set = pd.read_csv("Housing.csv")
data_set = data_set.replace({"yes": 1, "no": 0})
data_set.head()

total = sum(data_set.price)
no_elements = (len(data_set.price))
print(total/no_elements)
data_set = pd.get_dummies(data_set, columns=['furnishingstatus'])
X = data_set.drop("price",axis=1)
y = data_set["price"]

data_set.head()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)



regressor = RandomForestRegressor(n_estimators=100, random_state=42)

regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
y_true = y_test


for n in y_pred:
    clean_pred = []
    clean_pred.append(int(n))
    
    
    
for n in y_true:
    clean_true = []
    clean_true.append(int(n))
    
accuracy = accuracy_score(clean_true,clean_pred)

regressor.predict([[8000,4,2,3,1,0,0,0,1,3,1,1,0,0]])

pickle.dump(regressor,open('random_forest_nd.pkl','wb'))

mae = mean_absolute_error(y_test,y_pred)
mae





