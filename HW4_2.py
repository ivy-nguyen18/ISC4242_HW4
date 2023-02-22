'''
Design a program that uses matplotlib package to draw the graph of the following three-dimensional
surface:
𝑧 = 𝑔(𝑥, 𝑦) = {
𝑥
3 − 𝑦
3
3𝑥
2 + 5𝑦
2
. (𝑥, 𝑦) ≠ (0,0),
0, (𝑥, 𝑦) = (0.0).
over the domain [−2,2] × [−2,2].
Evaluate the directional derivative of the function 𝑔(𝑥, 𝑦) at the origin in the direction of the following
unit vector:
𝒖 = 〈
1
√2
,
1
√2
〉
Can you apply the following formula for the directional derivative?
𝐷𝒖𝑔(0,0) = ∇𝑔(0,0) ∙ �
'''

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def f(x,y):
    return np.where((y == 0) & (x == 0), 0, (x**3 - y**3)/((3*x**2) + (5*y**2)))

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

X = np.linspace(-2, 2, 501)
Y = np.linspace(-2, 2, 501)
X, Y = np.meshgrid(X, Y)

Z = f(X,Y)
surf = ax.plot_surface(X, Y, Z, cmap=cm.cool, linewidth=0, antialiased=False)
plt.show()

'''
You can not apply the directional derivative formula because the equation will be evaluated to equal (1/sqrt2)(0/0) + (1/sqrt2)(0/0).
However, before even evaluating the equation, checking if the function meets the requirements
of the directional derivative formula, the limit does not exist at g(0,0), thus you can't take the directional derivative at this point.
'''