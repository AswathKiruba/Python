import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic_df =pd.read_csv('C:/Users/aswat/Downloads/train.csv')
print(titanic_df)

print("Column Names")
print(titanic_df.columns.values)

print("Data Info")
print(titanic_df.info())

print("####################Null#########################")
print(titanic_df.isnull().sum())	

df = titanic_df.copy()
print("#########Data####Cleaning")

df.Embarked[df.Embarked.isnull()]=df.Embarked.dropna().mode().values



print(df.isnull().sum())

df1 = df.copy()

print("#########Setting average values#########")

df["Age"][df["Age"].isnull()] = df["Age"].mean()



print("**********Replace**********")
df["Cabin"][df["Cabin"].isnull()] = 'U0' 

print(df.isnull().sum())

survived_by_sex = df.groupby('Sex')['Survived'].mean()


print("************Visualization************8")
#df['Age'].hist(bin=70)


#sns.factorplot('Sex',data=df,kind="count")

#sns.kdeplot(df['Age'])

#sns.pairplot(df1,hue='Embarked')

def male_female_child(passenger):
    age,sex = passenger
    
    if age<16:
        return 'child'
    else:
        return sex

		
		
df['person'] = df[['Age','Sex']].apply(male_female_child,axis=1)

print(df.isnull().sum())



#from sklearn.preprocessing import LabelEncoder, OneHotEncoder

dummies = pd.get_dummies(df['person'])

df1 = df.drop(['person'],axis=1)

df1=pd.concat([df1,dummies],axis=1)

print(df1.columns.values)


Y = np.ravel(Y)

logmodel = LogisticRegression()

X_train,X_test,Y_train,Y_test = sklearn.model_selection.train_test_split(X,Y)

logmodel.fit(X,Y)


#predict based on the X_test data

class_predict = logmodel2.predict(X_test)

metrics.accuracy_score(Y_test,class_predict)