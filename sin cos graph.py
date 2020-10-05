import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10,0.1)
a=np.sin(x)
b=np.cos(x)
plt.plot(x,a,'b',linewidth=2,label="sin")
plt.plot(x,b,'r',linewidth=2,label="cos")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend(loc= "upper right")
plt.title("sin cos line graph")
plt.show()
