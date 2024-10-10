import matplotlib.pyplot as plt
import numpy as np

points = int(input('amount of points here: '))
sprile = int(input('spirals (golden ration 5): '))
golden_ratio = (1 + np.sqrt(sprile)) / 2
theta_max = 4 * np.pi

def golden_spiral(n_points=points):
    theta = np.linspace(0, theta_max, n_points)
    r = np.exp(theta / golden_ratio)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x, y = golden_spiral()

plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.axis('equal')
plt.show()