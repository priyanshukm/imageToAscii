from PIL import Image
import numpy as np
import sys

symbols = ['.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']
#symbols = symbols[::-1]

def to_ascii(p):
  ind = (p // 255) * (len(symbols) - 1)
  return symbols[ind]

size = 220, 220
def resize_image(image):
  image.thumbnail(size, Image.ANTIALIAS)
  return image

def gen_art(image, old_pixels):
  ascii_art = [to_ascii(c) for c in old_pixels]

  width, height = image.size
  pix = np.array(ascii_art).reshape(height, width)

  fin = []
  for x in pix:
    fin.append(''.join(x))
  fin = '\n'.join(fin)
  return fin

def read_from_file(filename):
  image = Image.open(filename).convert('L')
  return image

def write_to_file(filename, data):
  f = open(filename, "w")
  f.write(data)

image = read_from_file(sys.argv[1])
image = resize_image(image)
art = gen_art(image, list(image.getdata()))
print(art)
write_to_file(sys.argv[2], art)
