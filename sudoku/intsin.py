import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def func(x):
    return np.sin(x)

#y=func(x)を表示
x = np.linspace(-0.5, 3.5)
y = func(x)
fig, ax = plt.subplots(figsize=(8,8))
ax.axis([-0.5, 3.5, -2, 2])
ax.plot(x, y, 'b', linewidth=2)

# Make the shaded region
a, b = 0, np.pi / 2  # integral limits
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.text(0.65 * (a + b), 0.3, r"$\int_0^{\frac{\pi}{2}} \sin{x} \mathrm{d}x$", horizontalalignment='center', fontsize=20)
ax.text(3, 0.6, r"$y = \sin{x}$", horizontalalignment='center', fontsize=20)

ax.set_xticks((a, b, np.pi))
ax.set_xticklabels(('', r'$\frac{\pi}{2}$', r'$\pi$'))
ax.set_yticks([-1, 1])
ax.set_yticklabels(('-1', '1'))
ax.tick_params(labelsize=20)
fig.text(0.24, 0.45, '0', fontsize=20)

# 座標軸を原点を通る位置に移動
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.title('The area of the shaded part', fontsize=30)
# fig.savefig('intsin.svg')
plt.show()
