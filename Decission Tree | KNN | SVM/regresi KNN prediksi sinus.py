from sklearn.neighbors import KNeighborsRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FileDB = 'sinus.txt'
Database = pd.read_csv(FileDB, sep=",",header=0)
print("=================================")
print(Database)

x = Database[[u'Feature']]
y = Database.Target

regr = KNeighborsRegressor(n_neighbors=1)

regr.fit(x.values,y)

xx =np.arange(1, 21, 1)
n = len (xx)
print("xx(i)   K-NN")
for i in range (n) :
    y_neighbor = regr.predict([[xx[i]]])
    print('(:.2f)'.format(xx[i]), y_neighbor)

y_neighbor2= regr.predict(x)
plt.figure()
plt.plot(y_neighbor2, color ='red')
plt.scatter(x, y, color ='blue')
plt.title ('prediksi data menggunakan KNN')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['K-NN', 'data'], loc=2)
plt.show()
                    
