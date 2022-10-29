from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FileDB = 'sinus.txt'
Database = pd.read_csv(FileDB, sep=",",header=0)
print("=================================")
print(Database)

x = Database[[u'Feature']]
y = Database.Target

regr = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(200,200),
		    random_state=1, max_iter=100000, warm_start=True)

regr.fit(x.values,y)

xx =np.arange(1, 21, 1)
n = len (xx)
print("xx(i)   neural network")
for i in range (n) :
    y_neural = regr.predict([[xx[i]]])
    print('(:.2f)'.format(xx[i]), y_neural)

                    
