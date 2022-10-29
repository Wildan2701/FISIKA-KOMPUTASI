
from sklearn.svm import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FileDB = 'sinus.txt'
Database = pd.read_csv(FileDB, sep=",",header=0)
print("=================================")
print(Database)

x = Database[[u'Feature']]
y = Database.Target


svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_rbf.fit (x.values, y)


xx = np.arange(1, 21, 1)
n = len (xx)
                           
print ("-----------------------------------")
print ("-----------Predikei SVM------------")
print ("xx(i) rbf")
for i in range (n):
       rbf = svr_rbf.predict([[xx[i]]])
       print ('(:,2f)'.format(xx[i]),rbf)
print ("-----------------------------------")

rbf2 = svr_rbf.predict(x)
plt.figure ()
plt.plot (x, rbf2, color='red')
plt.scatter (x,y, color='blue')
plt.title ("Prediksi Data Menggunakan SVM")
plt.xlabel ('x')
plt.ylabel('y')
plt.legend (['rbf', 'data'],loc=2)
plt.show ()
