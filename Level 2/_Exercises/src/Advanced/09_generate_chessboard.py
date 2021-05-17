import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

squares = 8
pixels = 50

def blackAndWhite():
    'generator to yield black and white pixels'
    n = 0
    while(True):
        if n < pixels*squares // 2:
            for _ in range(pixels): yield [0, 0, 0]
            for _ in range(pixels): yield [255, 255, 255]
        else:
            for _ in range(pixels): yield [255, 255, 255]
            for _ in range(pixels): yield [0, 0, 0]
        n += 1
        n %= pixels*squares
        
g = blackAndWhite()
image = np.array([next(g) for row in range(pixels*squares) for col in range(pixels*squares)])
image = image.reshape(pixels*squares,pixels*squares,3)
print(image)
plt.imshow(image)
plt.show()

image = Image.fromarray(image.astype(np.uint8))
image.save("chessboard.jpeg")
