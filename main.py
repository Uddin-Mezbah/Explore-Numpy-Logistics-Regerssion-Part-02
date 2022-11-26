######################################
#                                    #
# MD MEZBAH UDDIN                    #
# Nantong University(China)          #
# CSE                                #
#                                    #
######################################


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv('HR_comma_sep.csv')
# print(data.size)
#step 1:MISSING data for any column
# print(data.isnull().values.any())

#step 2: check data type

# print(data.dtypes)
# print(data.salary.unique())

clean_up_values = {
    "salary": {
        'low': 1,
        'medium': 2,
        'high': 3
    }
}

data.replace(clean_up_values,inplace=True)
# print(data)
#step-4 get dummies for the Department
 
dummies = pd.get_dummies(data.Department)
# print(dummies)
merged = pd.concat([data,dummies],axis='columns')
# print(merged)

final_data = merged.drop(['Department','technical'],axis='columns')
print(final_data)
print(list(final_data.columns))
print('Department' in list(merged.columns))

# data with figure

plt.scatter(x=final_data.salary,y=final_data.left)
plt.scatter(x=final_data.satisfaction_level,y=final_data.left)
plt.scatter(x=final_data.time_spend_company, y=final_data.left)

plt.show()

# x = final_data.drop('left',axis='columns')
# y = final_data.left


# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# model = LogisticRegression()
# model.fit(x_train,y_train)

# accuracy = model.score(x_test,y_test)
# print(accuracy)
