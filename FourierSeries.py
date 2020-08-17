import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap

plt.rcParams['figure.figsize'] = [9, 9]
plt.rcParams.update({'font.size': 10})


# define our domain
dx = 0.001
L = np.pi
# defining our x line domain
x_line = L * np.arange(-1 + dx, 1 + dx, dx)
# n is the number of dots on our x line
n = len(x_line)
n_quarter = int(n/4)


# define hat function
f = np.zeros_like(x_line)
f[n_quarter:2 * n_quarter] = (4 / n) * np.arange(1, n_quarter + 1)
f[2*n_quarter:3*n_quarter] = np.ones(n_quarter) - (4/n)*np.arange(0, n_quarter)
fig, axs = plt.subplots(2)
axs[0].plot(x_line, f, '-', color='k', LineWidth=1)

# define rectangular function function
f2 = np.zeros_like(x_line)
f2[n_quarter: 3*n_quarter] = 1
axs[1].plot(x_line, f2, '-', color='b', LineWidth=1)

# compute fourier series
name = "accent"
cmap = get_cmap('tab10')
colors = cmap.colors
axs[0].set_prop_cycle(color=colors)

A01 = np.sum(f * np.ones_like(x_line)) * dx
fFs1 = A01/2
A1 = np.zeros(20)
B1 = np.zeros(20)
for k in range(20):
    A1[k] = np.sum(f * np.cos(np.pi*(k+1)*x_line/L)) * dx
    B1[k] = np.sum(f * np.sin(np.pi)*(k+1)*x_line/L) * dx
    fFs1 = fFs1 + A1[k]*np.cos((k+1)*np.pi*x_line/L) + \
        B1[k]*np.sin((k+1)*np.pi*x_line/L)
    axs[0].set_title('Fourier series for hat function:')
    axs[0].plot(x_line, fFs1, '-')

A02 = np.sum(f2 * np.ones_like(x_line)) * dx
fFs2 = A02/2
A2 = np.zeros(20)
B2 = np.zeros(20)
for k in range(20):
    A2[k] = np.sum(f2 * np.cos(np.pi*(k+1)*x_line/L)) * dx
    B2[k] = np.sum(f2 * np.sin(np.pi)*(k+1)*x_line/L) * dx
    fFs2 = fFs2 + A2[k]*np.cos((k+1)*np.pi*x_line/L) + \
        B2[k]*np.sin((k+1)*np.pi*x_line/L)
    axs[1].set_title('Fourier series for rectangular function:')
    axs[1].plot(x_line, fFs2, '-')

plt.show()
