import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,.5)
y = np.sin(x)
print(x)
print(y)
plt.plot(x,y)
plt.show()