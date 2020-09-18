import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,8))
ax.axis([0, 1, 0, 1])
ax.set_axis_off()

text = r'$\lim_{x \to 0} \ \frac{\arctan{x}}{\tanh{x}}$'
ax.text(0, 1, text, horizontalalignment='left', fontsize=30)

fig.savefig('e.svg')
# plt.show()
