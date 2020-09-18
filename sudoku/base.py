import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return np.sin(x) #関数


fig, ax = plt.subplots()
plt.axis([-0.5, 3.5, -2, 2]) #座標の表示領域
x = np.linspace(-0.5, 3.5) #関数の定義域
y = func(x)
ax.plot(x, y, 'b', linewidth=2)

# 座標軸を原点を通る位置に移動
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.tick_params(labelsize=20)

plt.title('Base', fontsize=30)

plt.show()
