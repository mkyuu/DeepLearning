import numpy as np
import matplotlib.pyplot as plt
 
sigma = 1  # 標準偏差
mu = 0  # 平均値

x =np.linspace(-5, 5)
y = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2 / (2*sigma**2))  # 確率密度関数

plt.plot(x, y)
plt.show()