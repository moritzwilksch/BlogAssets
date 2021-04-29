# %%
import multiprocessing as mp
import gif
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union
import matplotlib as mpl
mpl.rcParams['xtick.labelsize'] = 14
mpl.rcParams['ytick.labelsize'] = 14
gif.options.matplotlib["dpi"] = 100
# %%


def f(x: Union[float, np.ndarray]) -> float:
    return 2/3 * x**3 + 3*x**2 + 4*x + 2


def t1(x=None):
    return np.full_like(x, 2/3, dtype=np.float)


def t2(x=None):
    return 1.5 * x + 1.417


def f1(x):
    return 2*x**2 + 6*x + 4


def get_tangent_line(at_x, xs):
    m = f1(at_x)
    y = f(at_x)
    n = y - m*at_x
    return m * xs + n


# %%
xs = np.arange(-4, 0.1, 0.01)
ys = f(xs)

# %%

fig, ax = plt.subplots(figsize=(8, 6))


ax.set(
    xticks=range(-4, 2),
    xlim=(-4,1),
    xticklabels=range(-4, 2),
    yticks=range(-1, 3),
    ylim=(-1,3),
    yticklabels=[-1, '', 1, 2],
    aspect='equal'
)

# ax.set_title("Plot of $f(x)$", fontsize=18, family='Arial', weight='bold')

ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
plt.grid(which='both', ls='--', c='0.8')

ax.plot(xs, ys, color='blue', label='$f(x)$')

t1_xs = np.arange(-3, 0, 1)
t2_xs = np.arange(-1, 1, 1)

ax.plot(t1_xs, t1(t1_xs), c='r', label='Tangent at $x=-2$')
ax.plot(t2_xs, t2(t2_xs), c='g', label='Tangent at $x=-0.5$')
ax.scatter(x=-2, y=2/3, marker='o', c='r')
ax.scatter(x=-0.5, y=2/3, marker='o', c='g')
plt.savefig("two_tangents.png", dpi=200, facecolor='white')
# plt.legend(fontsize=14)


# %%
# GIF

@gif.frame
def plot_frame(x):
    fig, ax = plt.subplots(figsize=(8, 6))


    ax.set(
        xticks=range(-4, 2),
        xlim=(-4, 1),
        xticklabels=range(-4, 2),
        yticks=range(-1, 3),
        ylim=(-1, 3),
        yticklabels=[-1, '', 1, 2],
        aspect='equal'
    )

    # ax.set_title("Plot of $f(x)$", fontsize=18, family='Arial', weight='bold')

    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    plt.grid(which='both', ls='--', c='0.8')

    xs = np.arange(-3, 0.1, 0.01)
    ys = f(xs)
    ax.plot(xs, ys, color='blue', label='$f(x)$')

    tangent_xs = np.arange(x-0.5, x+0.6, 0.1)
    ax.plot(tangent_xs, get_tangent_line(x, tangent_xs), c='g')
    ax.scatter(x=x, y=f(x), marker='o', c='g')

    ax.text(x=-1.5, y=-0.5, s=f"$x={x:.2f}$\n$f'(x) = {f1(x):.2f}$", size=16, color='g',
            bbox={'facecolor': 'white', 'alpha': 1, 'edgecolor': 'k', 'pad': 5}, ha='center', va='center')
    plt.tight_layout()

def calc_steps(start_x, gamma=0.001, f1=None, n=100):
    xs = [start_x]
    for i in range(n):
        xs.append(xs[-1] + (- gamma * f1(xs[-1])))
    return xs


# %%
frames = [plot_frame(x) for x in calc_steps(start_x=-0.1, gamma=0.1, f1=f1, n=20)]
gif.save(frames, 'gradient_descent.gif', duration=300)


#%%
frames = [plot_frame(x) for x in calc_steps(start_x=-0.1, gamma=0.7, f1=f1, n=6)]
gif.save(frames, 'diverging_gradient_descent.gif', duration=500)

#%%
# plot_frame(-0.1)