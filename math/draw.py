import numpy as np  
import matplotlib.pyplot as plt  
  
#t = np.arange(0.0, 1.01, 0.01)  
#s = np.sin(2*2*np.pi*t) 
#plt.fill(t, s*np.exp(-5*t), 'r')  
#plt.grid(True)  

x = np.arange(-5, 5, 0.01)
y = x*x + 5*x + 6
z = x*0
# a = -5*x -6 
plt.plot(x,y,'red')
plt.plot(x,z,'green')
#plt.plot(x,a,'blue')

plt.show()  
