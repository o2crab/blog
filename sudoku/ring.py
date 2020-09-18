import numpy as np
import matplotlib.pyplot as plt

delta = 0.025
xrange = np.arange(-1.1, 1.1, delta)
yrange = np.arange(-1.1, 1.1, delta)
X, Y = np.meshgrid(xrange, yrange)

#目盛りの間隔を揃える
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
plt.axis([-1.1, 1.1, -1.1, 1.1])
ax.set_xticks([-np.sqrt(2)/np.sqrt(np.pi), 1/np.sqrt(np.pi), 0, np.sqrt(2)/np.sqrt(np.pi), 1/np.sqrt(np.pi)])
ax.set_yticks([-np.sqrt(2)/np.sqrt(np.pi), 1/np.sqrt(np.pi), 0, np.sqrt(2)/np.sqrt(np.pi), 1/np.sqrt(np.pi)])
txt1 = r'$\frac{1}{\sqrt{\pi}}$'
txt2 = r'$\frac{\sqrt{2}}{\sqrt{\pi}}$'
plt.xticks([-np.sqrt(2)/np.sqrt(np.pi), -1/np.sqrt(np.pi), 0, 1/np.sqrt(np.pi), np.sqrt(2)/np.sqrt(np.pi)], [r'$-$' + txt2, r'$-$' + txt1, 0, txt1, txt2])
plt.yticks([-np.sqrt(2)/np.sqrt(np.pi), -1/np.sqrt(np.pi), 0, 1/np.sqrt(np.pi), np.sqrt(2)/np.sqrt(np.pi)], [r'$-$' + txt2, r'$-$' + txt1, 0, txt1, txt2])
ax.tick_params(labelsize='25', pad=-50, direction='in')
plt.grid(b=True)
plt.gca().set_aspect('equal', adjustable="box")
plt.title('The area of this ring', fontsize=30)


Z = X**2 + Y**2
CS = plt.contourf(X, Y, Z, [1 / np.pi, 2 / np.pi], colors=['#6c0'])

plt.plot([-1/np.sqrt(np.pi), -1/np.sqrt(np.pi), 1/np.sqrt(np.pi), 1/np.sqrt(np.pi), -1/np.sqrt(np.pi)], [-1/np.sqrt(np.pi), 1/np.sqrt(np.pi), 1/np.sqrt(np.pi), -1/np.sqrt(np.pi), -1/np.sqrt(np.pi)], 'r--', lw='3')

# plt.title(r'$x^n + y^n = 0.01$', fontsize=30)
fig.savefig('ring.svg')
