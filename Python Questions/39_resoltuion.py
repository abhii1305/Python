# program to find the size or resolution of a image using pillo module

import PIL
from PIL import Image
import PIL.Image

img = PIL.Image.open("C:/Users/abhij/OneDrive/Pictures/20230405_230854 (1)")
width, height = img.size

print(width,'x',height)