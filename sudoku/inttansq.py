import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def func(x):
    return 1 + np.tan(x)**2

#y=func(x)を表示
x = np.arange(-2, 3.5, 0.01)
y = func(x)
fig, ax = plt.subplots(figsize=(8,8))
ax.axis([-2, 3.5, -2, 100])
ax.plot(x, y, 'b', linewidth=2)

# Make the shaded region
a, b = 0, (np.pi / 2)-0.001  # integral limits, pi/2だとshadedにならない
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

ax.text(0.48, 70, r"$y = (1 + \tan^2 x)$", horizontalalignment='center', fontsize=20)
# ax.text(3, 25, r"$\int_0^{\frac{\pi}{2}} (1 + \tan^2 x) \mathrm{d}x$", horizontalalignment='center', fontsize=20)
arrowtext = r"$\int_0^{\frac{\pi}{2}} (1 + \tan^2 x) \mathrm{d}x$"
ax.annotate(arrowtext, xy=(1.45, 7.5), xytext=(2, 25), arrowprops=dict(facecolor='black'), fontsize=20)

ax.set_xticks((a, b, np.pi))
ax.set_xticklabels(('', r'$\frac{\pi}{2}$', r'$\pi$'))
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
# fig.savefig('inttansq.svg')
plt.show()
