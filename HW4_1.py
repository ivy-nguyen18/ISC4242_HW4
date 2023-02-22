'''
Design a program that draws the graph of the following function on the interval [-10,10]:
𝑦 = 𝑓(𝑥) = {
sin(1/𝑥), 𝑥 ≠ 0,
0, 𝑥 = 0.
'''
import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    if x == 0:
        return 0
    else:
        return math.sin(1/x)

x = np.linspace(-10,10,501)
y = []
for i in x:
    y.append(f(i))

plt.plot(x, y, 'r-')
plt.show()

