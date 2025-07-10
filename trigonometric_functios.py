import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-np.pi/2,np.pi/2,2000)
x_tg=x[np.cos(x)!=0]
x_ctg=x[np.sin(x)!=0]
y_sin=np.sin(x)
y_cos=np.cos(x)
y_tg=np.tan(x)
y_ctg=1/np.tan(x)
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.plot(x,y_tg)
plt.plot(x,y_ctg)
plt.ylim(-10,10)
#plt.xlim(-2*np.pi,2*np.pi)
plt.xlabel('x')
plt.ylabel("y")
plt.grid(True)
plt.show()