import matplotlib.pyplot as plt
import numpy as np
import math
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False   

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.title(r'$y=e^{-t}cos(2\pi t)$')

plt.subplot(212)
x = np.arange(1,5)
plt.plot(x, 3*x, 'r--') # r, g, b, k
plt.plot(x, np.exp(x), 'b^') # -和--虚线, s正方形, ^三角形
plt.legend(labels = ('exp','log'),loc='upper left')

plt.show()
