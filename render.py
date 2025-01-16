import os
import glob
from PIL import Image, ImageOps

size = 3600, 2400

pwd = os.path.join(os.getcwd(), "orig", "**/*")
savepwd = os.path.join(os.getcwd(), "half_size")

file_list = [f for f in glob.iglob(pwd, recursive=True) if os.path.isfile(f)]

background = Image.new('RGB', size, (255, 255, 255))
counter = 0
for f in file_list:
    print(counter)
    print(f)
    counter += 1
    if counter % 2 == 1:
        background = Image.new('RGB', size, (255, 255, 255))
    img = Image.open(f)
    img = ImageOps.exif_transpose(img)
    if img.size[0] > img.size[1]:
        img = img.rotate(90, expand=True)
    if img.size[1] / img.size[0] > 2400/1800:
        ratio = size[1] / float(img.size[1])
        img = img.resize((int(ratio * img.size[0]), size[1]), Image.Resampling.LANCZOS)
    else:
        ratio = (size[0] / 2) / float(img.size[0])
        img = img.resize((int(size[0] / 2), int(ratio * img.size[1])), Image.Resampling.LANCZOS)
    offset = 0, 0
    if counter % 2 == 0:
        offset = size[0]-img.size[0],0
    print("offset: " + str(offset))
    background.paste(img, offset)
    if counter % 2 == 0:
        background.save(os.path.join(savepwd, str(counter) + '.jpeg'))

if counter % 2 == 1:
    background.save(os.path.join(savepwd, str(counter) + '.jpeg'))
