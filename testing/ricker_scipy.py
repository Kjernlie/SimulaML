from scipy import signal
import matplotlib.pyplot as plt
import seaborn as sns

points = 100
a = 4.0
vec2 = signal.ricker(points, a)
plt.plot(vec2)
plt.legend(['Mexican hat wavelet'])
plt.show()
