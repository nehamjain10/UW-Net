import rawpy
import numpy as np
import imageio
import os

os.makedirs("seathru_jpg",exist_ok=True)

def save_image(filepath,number):
  #Loading the RGB image
  with rawpy.imread(filepath) as raw1:
      rgb=raw1.postprocess()
      imageio.imwrite(f"seathru_jpg/{number}.jpg",rgb)
      print(number,'DONE')

L=os.listdir("seathru_raw")

for count,i in enumerate(L):
    save_image("seathru_raw/"+i,count)
