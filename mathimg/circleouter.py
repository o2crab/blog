import numpy as np
import matplotlib.pyplot as plt
# {
# # # x = np.linspace(0, 2, 100)
# # # fig, ax = plt.subplots()
# # # ax.plot(x, x, label="linear")
# # # ax.plot(x, x**2, label="quadratic")
# # # ax.plot(x, x**3, label="cubic")
# # # ax.set_xlabel('x label')
# # # ax.set_ylabel('y label')
# # # ax.set_title('Simple Plot')
# # # ax.legend()
# # # plt.show()
# }
# {
# x = np.linspace(0, 2, 100)
# plt.plot(x, x, label="linear")
# plt.plot(x, x**2, label="quadratic")
# plt.plot(x, x**3, label="cubic")
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title('Simple Plot')
# plt.legend()
# plt.show()
# }

# def my_plotter(ax, data1, data2, param_dict):
#     out = ax.plot(data1, data2, **param_dict)
#     return out
#
# data1, data2, data3, data4 = np.random.randn(4, 100)
# fig, (ax1, ax2) =plt.subplots(1, 2)
# my_plotter(ax1, data1, data2, {'marker': 'x'})
# my_plotter(ax2, data3, data4, {'marker': 'o'})
# plt.show()

delta = 0.025
xrange = np.arange(-5.1, 5.1, delta)
yrange = np.arange(-5.1, 5.1, delta)
X, Y = np.meshgrid(xrange, yrange)

#目盛りの間隔を揃える
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
plt.axis([-5.1, 5.1, -5.1, 5.1])
ax.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
ax.set_yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
plt.grid(b=True)
plt.gca().set_aspect('equal', adjustable="box")

for n in range(2, 61, 2):
    Z = X**n + Y**n
    CS = plt.contour(X, Y, Z, [25], colors=['#4a0'])
    if n <= 6:
        ax.clabel(CS, inline=True, fmt='n='+str(n), fontsize=20)

plt.plot([-1, -1, 1, 1, -1], [-1, 1, 1, -1, -1], 'r--', lw='3')

plt.title(r'$x^n + y^n = 25$', fontsize=30)
fig.savefig('circle.svg')
plt.show()
