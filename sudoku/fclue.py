#sum 3/4^n のヒント

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))
ax.axis([-0.1, 1.1, -0.1, 1.1])
ax.set_axis_off()

plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color='#a50', linewidth=3)

ax.text(0.5, -0.1, "1", horizontalalignment='center', fontsize=20)
ax.text(-0.1, 0.5, "1", horizontalalignment='center', fontsize=20)

for n in range(1, 7):
    coord = 1 - 2**(-n)
    plt.plot([coord, 1], [coord, coord], color='#a50', linewidth=2)
    plt.plot([coord, coord], [coord, 1], color='#a50', linewidth=2)

fig.savefig('fclue.svg')
# plt.show()
