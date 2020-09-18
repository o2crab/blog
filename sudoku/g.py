import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,8))
ax.axis([0, 1, 0, 1])
ax.set_axis_off()

text = r'$-e^{i \pi},\ \ (i^2=-1)$'
ax.text(0, 1, text, horizontalalignment='left', fontsize=30)

fig.savefig('g.svg')
# plt.show()
