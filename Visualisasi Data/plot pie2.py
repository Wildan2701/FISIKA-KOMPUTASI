import matplotlib.pyplot as plt
labels = ['Lain-lain','Samsung','Apple','Huawei', 'Oppo', 'Vivo']
values = [42,21,14,9,8,7]
colors = ['red','green','pink','blue', 'yellow','orange']
explode = [0,0.3,0,0,0,0] #Fokus ke samsung
plt.pie(values,labels=labels,colors=colors,explode=explode,
shadow=True,autopct='%1.1f%%',startangle=180)
plt.axis('equal')
plt.show()
  
