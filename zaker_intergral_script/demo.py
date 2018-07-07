import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation



# animation function.  This is called sequentially
def animate(i):
    data = np.random.random((255, 255))
    im.set_array(data)
    return [im]


fig = plt.figure()
data = np.random.random((255, 255))
im = plt.imshow(data, cmap='gray')
anim = animation.FuncAnimation(fig, animate, frames=200, interval=60, blit=True)
plt.show()