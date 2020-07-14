# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:03:34 2020

@author: Mumes
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('salary_data_cleaned.csv')


#choose relevant columns
df.columns
# faltaria crear columnas 'comp_num' 'senority' 'job_simple' 'desc len'

df_model = df[['avg_salary','Rating', 'Size','Type of ownership', 'Industry', 'Sector', 'hourly',
               'job_state', 'age','python_yn','spark_yn', 'excel_yn','aws_yn']]
#get dummy data
df_dum = pd.get_dummies(df_model)

#train test split
from sklearn.model_selection import train_test_split

X=df_dum.drop('avg_salary', axis=1)
y= df_dum['avg_salary'].values  # .values crea un array, sino seria simplemente una serie

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#multilinear regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X)
model.fit().summary()

from sklearn.linear_model import LinearRegression,Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

cross_val_score(lm, X_train,y_train,scoring = 'neg_mean_absolute_error',cv =3)
np.mean(cross_val_score(lm, X_train,y_train,scoring = 'neg_mean_absolute_error',cv =3))

#laso regression
lml = Lasso(alpha=0.13)
lml.fit(X_train,y_train)
np.mean(cross_val_score(lm_l, X_train,y_train,scoring = 'neg_mean_absolute_error',cv =3))

alpha =[]
error = []

for i in range(1,500):
    alpha.append(i/100)
    lm_l = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lm_l, X_train,y_train,scoring = 'neg_mean_absolute_error',cv =3)))
plt.plot(alpha,error)
 
#random forest
from sklearn.ensemble import RandomForestRegressor
rf= RandomForestRegressor()
np.mean(cross_val_score(rf, X_train,y_train,scoring ='neg_mean_absolute_error',cv =3))

#tune model GridsearchCV

from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,100,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}
gs = GridSearchCV(rf, parameters, scoring ='neg_mean_absolute_error',cv =3)
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_
#test ensambles
tpred_lm = lm.predict(X_test)
tpred_lml = lml.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lml)
mean_absolute_error(y_test, tpred_rf)