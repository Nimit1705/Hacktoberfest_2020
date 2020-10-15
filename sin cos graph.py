import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,20,0.2)
a=np.sin(x)
b=np.cos(x)
plt.plot(x,a,'b',linewidth=1.5,label="sin")
plt.plot(x,b,'r',linewidth=1.5,label="cos")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(loc= "upper right")
plt.title("sin(x) cos(x) line graph")
plt.show()
