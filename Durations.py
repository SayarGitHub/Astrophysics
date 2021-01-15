from math import *

import matplotlib.pyplot as plt
import numpy as np

lat = radians(32.783)
declinations = np.arange(-47.217, 57.217, 0.01)
durations = []
for i in declinations:
    i = radians(i)
    arg = -tan(i) * tan(lat)
    h = degrees(acos(arg))
    duration = 2 * abs(h) / 15
    durations.append(duration)
print(durations)

X = declinations
y = durations

plt.plot(X, y)
plt.xlabel("Declinations(in degrees)")
plt.ylabel("Durations(in degrees)")
plt.title("Visibility vs Declinations")
plt.savefig("Visibility vs Declinations.png", dpi=600)
plt.savefig("Visibility vs Declinations.pdf", dpi=600)
plt.show()
