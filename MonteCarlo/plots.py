# %%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dataclasses import dataclass
import gif
from sklearn.inspection import plot_partial_dependence
gif.options.matplotlib["dpi"] = 150
plt.rcParams['font.family'] = 'Arial'
# %%


def is_in_circ(xs, ys, cx, cy, r):
    return (xs-cx)**2 + (ys-cy)**2 <= r**2
# %%


fig, ax = plt.subplots(figsize=(10, 5))
# create some circles
circle1 = plt.Circle((-2, -1), 3, color='r', alpha=.3)
circle2 = plt.Circle((3, 3), 6, color='b', alpha=.3)

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.set_xlim(-7, 10)
ax.set_ylim(-5, 10)
ax.set_aspect('equal')

sns.despine(fig)
ax.spines['bottom'].set_position('zero')
ax.grid(which='both', ls='--', c='0.8')
ax.set_axisbelow(True)


# %%
XLIM = (-7, 10)
YLIM = (-5, 10)

# %%
fig, ax = plt.subplots(figsize=(10, 5))
# create some circles
circ1 = (-2, -1), 3
circ2 = (3, 3), 6
circle1 = plt.Circle(*circ1, color='r', alpha=.3)
circle2 = plt.Circle(*circ2, color='b', alpha=.3)

ax.add_artist(circle1)
ax.add_artist(circle2)
ax.set_xlim(XLIM)
ax.set_ylim(YLIM)
ax.set_aspect('equal')

sns.despine(fig)
ax.spines['bottom'].set_position('zero')
ax.grid(which='both', ls='--', c='0.8')
ax.set_axisbelow(True)


# %%
STEPS = 150
xs = np.random.uniform(*XLIM, size=(110, STEPS))
ys = np.random.uniform(*YLIM, size=(110, STEPS))


@gif.frame
def point_rain(step):

    fig, ax = plt.subplots(figsize=(10, 5))

    circle1 = plt.Circle((-2, -1), 3, color='r', alpha=.3)
    circle2 = plt.Circle((3, 3), 6, color='b', alpha=.3)

    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.set_xlim(XLIM)
    ax.set_ylim(YLIM)
    ax.set_aspect('equal')

    sns.despine(fig)
    ax.spines['bottom'].set_position('zero')
    ax.grid(which='both', ls='--', c='0.8')
    ax.set_axisbelow(True)

    xflat = xs[:step].ravel()
    yflat = ys[:step].ravel()

    is_in_intersection = (
        is_in_circ(xflat, yflat, circ1[0][0], circ1[0][1], circ1[1])
        & is_in_circ(xflat, yflat, circ2[0][0], circ2[0][1], circ2[1])
    )

    ax.scatter(
        xflat[is_in_intersection],
        yflat[is_in_intersection],
        color='yellow',
        s=6,
        alpha=0.8,
        zorder=10
    )

    ax.scatter(
        xflat[~is_in_intersection],
        yflat[~is_in_intersection],
        color='k',
        s=6,
        alpha=0.25
    )

    fig.suptitle(f"Points in Intersection: {is_in_intersection.mean() if step > 0 else 0:.3%}",
                 size=18, weight='bold')

    ax.set_title(
        f"Total Points: {len(xflat):,}",
        size=14,
    )

    
frames = [point_rain(x) for x in range(STEPS)]
gif.save(frames, "pointrain.gif")

# point_rain(50)
