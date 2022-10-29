import sklearn.neural_network import MLPClassifier
import pandas as pd

#Database : Gerbang Logika And
#Membaca data dari file
FileDB = 'logikaAND.txt'
#file dapat berpa csv,txt dll
Database = pd.read_txt(FileDB, sep=",",header=0)
print(Database)

#x = Data, y = Target
x = Database[[u'Feature1', u'Feature2']]
y = Database.Target

#Training dan Classifiy
clf = MLPClassifier(solver='lbfgs', alpha=le-2,hidden_layer_size=(10, 5),
		    random_state=1, max_iter=1000, warm_start=True)
clf.fit(x, y)

#Prediksi
print ("Logika AND MEtode Artificial Neural Network (ANN)")
print ("Logika = Prediksi")
print ("0 0 = ", clf.predict([[0, 0]]))
print ("0 1 = ", clf.predict([[0, 1]]))
print ("1 0 = ", clf.predict([[1, 0]]))
print ("1 1 = ", clf.predict([[1, 1]]))
