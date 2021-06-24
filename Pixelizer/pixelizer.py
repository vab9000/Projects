"""Pixelizes an image"""
from PIL import Image
PIXELIZATION_GRADIENT = 20
if PIXELIZATION_GRADIENT is None:
    try:
        PIXELIZATION_GRADIENT = int(input('Pixelization Gradient: '))
    except ValueError:
        print('Legal values must be a number that is 1 or greater')
    if PIXELIZATION_GRADIENT <= 0:
        print('Legal values must be a number that is 1 or greater')
        quit()
img = Image.open(
    '/Users/home/varun/Projects/Pixelizer/wikipedia.png'
    )
pixelMap = img.load()
img2 = Image.new(
    img.mode,
    (
        int(img.size[0]/PIXELIZATION_GRADIENT),
        int(img.size[1]/PIXELIZATION_GRADIENT)
        )
    )
pixelsNew = img2.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        try:
            pixelsNew[
                int(i/PIXELIZATION_GRADIENT),
                int(j/PIXELIZATION_GRADIENT)
                ] = pixelMap[i, j]
        except IndexError:
            pass
img.close()
img2.show()
img2.save("/Users/home/varun/Projects/Pixelizer/new_image.png")
img2.close()
