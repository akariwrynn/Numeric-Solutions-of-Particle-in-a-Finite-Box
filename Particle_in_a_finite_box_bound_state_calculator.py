
import numpy as np
import matplotlib.pyplot as plt
import math

k=10 #k value defined earlier

x=np.arange(0,20,0.01) # The solution search array
y=np.zeros(len(x))
for i in range(len(x)):
    xi=x[i]
    y[i]=xi**2+xi**2*math.tan(xi/2)**2-k*math.pi**2 #Equation that is defined in the article
plt.semilogy(x,y)
plt.show()