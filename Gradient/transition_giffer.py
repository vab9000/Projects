"""Transitions 1 image to another"""
from time import time
from PIL import Image
import imageio
new_time = time()
GRADIENT_COUNT = 20
img = Image.open(
    '/Users/home/varun/Projects/Gradient/wikipedia.png'
    )
img2 = Image.open(
    '/Users/home/varun/Projects/Gradient/map.png'
    )
pixelMap = img.load()
img2 = img2.resize((img.size[0], img.size[1]))
pixelMap2 = img2.load()
pixel_gradients = list()
for i in range(img.size[0]):
    pixel_column = list()
    for j in range(img.size[1]):
        pixel_column.append((0, 0, 0, 0))
    pixel_gradients.append(pixel_column)
for i in range(img.size[0]):
    for j in range(img.size[1]):
        try:
            pixel_gradients[i][j] = (
                pixelMap[i, j][0] - pixelMap2[i, j][0],
                pixelMap[i, j][1] - pixelMap2[i, j][1],
                pixelMap[i, j][2] - pixelMap2[i, j][2],
                pixelMap[i, j][3] - pixelMap2[i, j][3]
            )
        except IndexError:
            pass
gradients = list()
k = 0
while k < GRADIENT_COUNT + 1:
    new_image = Image.new('RGBA', (img.size[0], img.size[1]), color='red')
    newPixelMap = new_image.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            try:
                newPixelMap[i, j] = (
                    int
                    (
                        pixelMap[i, j][0] - (
                            pixel_gradients[i][j][0]
                            ) * k / GRADIENT_COUNT
                        ),
                    int
                    (
                        pixelMap[i, j][1] - (
                            pixel_gradients[i][j][1]
                            ) * k / GRADIENT_COUNT
                        ),
                    int
                    (
                        pixelMap[i, j][2] - (
                            pixel_gradients[i][j][2]
                        ) * k / GRADIENT_COUNT
                    ),
                    int
                    (
                        pixelMap[i, j][3] - (
                            pixel_gradients[i][j][3]
                            ) * k / GRADIENT_COUNT
                    )
                )
            except IndexError:
                pass
    new_image.save(
        '/Users/home/varun/Projects/Gradient/gradients/gradient'
        + str(k)
        + '.png'
    )
    new_image.close()
    gradients.append(
        '/Users/home/varun/Projects/Gradient/gradients/gradient'
        + str(k)
        + '.png'
    )
    k += 1
img.close()
img2.close()
images = []
for filename in gradients:
    images.append(imageio.imread(filename))
imageio.mimsave('/Users/home/varun/Projects/Gradient/gradient.gif', images)
print('Took ' + str(int(time() - new_time)) + ' Seconds')
