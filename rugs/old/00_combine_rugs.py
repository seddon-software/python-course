from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

fig2 = np.load("rugs/fig2.npy")
fig3 = np.load("rugs/fig3.npy")
fig4 = np.load("rugs/fig4.npy")
print(fig2.shape)
print(fig3.shape)
print(fig4.shape)
fig = np.vstack((fig4,fig3))
print(fig.shape)

FIG = "figure"
np.save(f"rugs/{FIG}", fig)
plt.imshow(fig, cmap="gray")
plt.savefig(f"rugs/{FIG}.png")
plt.gcf().suptitle(f"{FIG}")
plt.show()


