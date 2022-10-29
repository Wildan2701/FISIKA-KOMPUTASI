from sklearn.tree import DecisionTreeRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FileDB = 'sinus.txt'
Database = pd.read_csv(FileDB, sep=",",header=0)
print("=================================")
print(Database)

x = Database[[u'Feature']]
y = Database.Target

regr = DecisionTreeRegressor(random_state=0)

regr.fit(x.values,y)

xx =np.arange(1, 21, 1)
n = len (xx)
print("xx(i)    Decission Tree")
for i in range (n) :
    y_det2 = regr.predict([[xx[i]]])
    print('(:.2f)'.format(xx[i]), y_det2)

y_det2 = regr.predict(x)
plt.figure()
plt.plot(x, y_det2, color ='red')
plt.scatter(x, y, color ='blue')
plt.title ('prediksi data menggunakan neural network')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Decission Tree', 'data'], loc=2)
plt.show()
                    
