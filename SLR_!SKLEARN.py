import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Calculating Mean
def fn_mean(temp) :
    return sum(temp)/len(temp)

#Calculating Covariance
def fn_cov(x,y) :
    covar = 0
    mean_x = fn_mean(x)
    mean_y = fn_mean(y)
    for i in range(0,len(x)) :
        covar += (x[i]-mean_x) * (y[i]-mean_y)
    return covar

#Calculating Variance
def fn_var(x) :
    var = 0
    mean_x = fn_mean(x)
    for i in range(0,len(x)):
        var += (x[i]-mean_x)**2
    return var

#Simple Linear Regression Model
def predict(X) :
    y_pred = np.array([0]*len(X))
    for i in range(0,len(X)) :
        y_pred[i] = b0 + b1*X[i]
    return y_pred


#Reading Dataset
dataset  = pd.read_csv("Salary_Data.csv")
dataset = dataset.sample(frac=1)

#Splitting dataset into Testing And Training sets
rows = int(dataset.shape[0] * (2/3))
X_train = dataset.iloc[:rows,0].values
X_test = dataset.iloc[rows:,0].values
y_train = dataset.iloc[:rows,1].values
y_test = dataset.iloc[rows:,1].values

#calculating b1 and b0
b1 = fn_cov(X_train,y_train)/fn_var(X_train)
b0 = fn_mean(y_train) - b1*fn_mean(X_train)

#Training set plot
plt.scatter(X_train,y_train,color = "yellow")
plt.plot(X_train,predict(X_train),color="red")
plt.title("Salary vs Years of Experience(Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
 
 #Test set plot
plt.scatter(X_test,y_test,color = "yellow")
plt.plot(X_train,predict(X_train),color="red")
plt.title("Salary vs Years of Experience(Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
 