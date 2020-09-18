import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,8))
ax.axis([0, 1, 0, 1])
ax.set_axis_off()

text = r'$\sum_{n=1}^{\infty} \frac{3}{4^{n}} \hspace{2} \ i.e. \hspace{2} \frac{3}{4} + \frac{3}{4^{2}} + \frac{3}{4^{3}} + \dots$'
ax.text(0, 1, text, horizontalalignment='left', fontsize=30)

# fig.savefig('f.svg')
plt.show()
