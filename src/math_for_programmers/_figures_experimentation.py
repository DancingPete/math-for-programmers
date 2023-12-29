import matplotlib.pyplot as plt

fig = plt.figure(
    layout="tight",
    figsize=(7, 7),
    facecolor="blue",
    edgecolor="wheat",
    frameon=True,
    visible=True,
)
fig.suptitle("Main Figure")

subfig1, subfig2 = fig.subfigures(1, 2)

subfig1.suptitle("SubFigure 1")
subfig1.set_facecolor("red")
subfig1.set_edgecolor("wheat")

subfig2.suptitle("SubFigure 2")
subfig2.set_facecolor("green")
subfig2.set_edgecolor("wheat")

plt.show()
