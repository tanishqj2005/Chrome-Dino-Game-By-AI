from PIL import Image, ImageGrab
import numpy as np
from numpy import asarray

if __name__ == "__main__":
    image = ImageGrab.grab().convert('L')
    width, height = image.size
    left = 0
    top = int(2*height / 7)
    right = 275
    bottom = int(4 * height / 7)
    im1 = image.crop((left, top, right, bottom))
    im1.show()