import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

np.random.seed(14)

x = list(range(1,6))
y = np.linspace(1,10,5)
fig, ax = plt.subplots()

def makebars(ax, x, y, w):
    for x, y in zip(x, y):
        bar = Rectangle((x, 0),w, y)
        ax.add_patch(bar)

makebars(ax, x, y, 0.4)

ax.autoscale()

fig.set_size_inches(15,5)#change the size of the fig

ax.set_title('Some bar chart') #gave a name to parts of graph
ax.set_xlabel('This is x label')
ax.set_ylabel('This is y label')

print(help(Rectangle))

ax.patches[0].set_alpha(0.3)#placed the first[0] with less color.

for r in ax.patches:
    r.set_edgecolor('g')
    r.set_ls('dashed')
    r.set_lw(3)
    r.set_hatch('\\')# placed the graph to dotted.

sketches = [0, 0.25, 0.5, 0.75, 1]

for r, s in zip(ax.patches, sketches):
    r.set_sketch_params(s)

makebars(ax, x, y, 0.8)

rec_id = range(10)

zorder = reversed(rec_id)

for r, z in zip(rec_id, zorder):
    ax.patches[r].set_zorder(z)

ax.patches[9].set_clip_on(False)

ax.set_xlim(0,5.4)
ax.set_ylim(0,9)

plt.show()