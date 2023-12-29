import matplotlib.pyplot as plt

# Define figure
fig = plt.figure(
    layout="constrained",
    facecolor="lightgreen",
)
fig.suptitle("Figure Title")

# Define axes
mosaic = [
    ["top", "top"],
    ["bottom-left", "bottom-right"],
]
axes = fig.subplot_mosaic(mosaic)

# Configure individual axes

# Top axes
ax_top = axes.get("top")
ax_top.set_title("Top Axes Title")
ax_top.set_xticks(range(-5, 6))
ax_top.set_yticks(range(-3, 4))
ax_top.text(
    0, 0,
    "This is test text",
    ha="center",
    va="center",
)

# Bottom left axes
ax_bleft = axes.get("bottom-left")
ax_bleft.set_title("Bottom Left Axes Title")

# Bottom right axes
ax_rleft = axes.get("bottom-right")
ax_rleft.set_title("Bottom Right Right Axes Title")
ax_bleft.scatter(2, 2)

plt.show()

