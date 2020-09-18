import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def func(x):
    return np.log(x)

#y=func(x)を表示
x = np.arange(0.01, 5, 0.01)
y = func(x)
fig, ax = plt.subplots(figsize=(8,8))
ax.axis([-1, 5, -3, 3])
ax.plot(x, y, 'b', linewidth=2)

# Make the shaded region
a, b = 1, np.e  # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.text(4, 1, r"$y = \log x$", horizontalalignment='center', fontsize=20)
# ax.text(3, 25, r"$\int_0^{\frac{\pi}{2}} \log x \mathrm{d}x$", horizontalalignment='center', fontsize=20)
arrowtext = r"$\int_1^e \log x \mathrm{d}x$"
ax.annotate(arrowtext, xy=(2, 0.3), xytext=(2.5, -1.5), arrowprops=dict(facecolor='black'), fontsize=20)

ax.set_xticks((a, b))
ax.set_xticklabels(('1','e'))
# ax.set_yticks([-1, 1])
# ax.set_yticklabels(('-1', '1'))
ax.tick_params(labelsize=20)

# 座標軸を原点を通る位置に移動
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.title('The area of the shaded part', fontsize=30, y=1.05)
fig.savefig('intlog.svg')
# plt.show()
