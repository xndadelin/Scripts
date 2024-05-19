# scrambled1.png and scrambled2.png are the images that are to be added
# The output is the image added.png

from PIL import Image
image1 = Image.open('/home/xndadelin/Desktop/Scripts/steg/scrambled1.png')
image2 = Image.open('/home/xndadelin/Desktop/Scripts/steg/scrambled2.png')

# Add the images, blend
image = Image.blend(image1, image2, alpha=0.5)
image.save('/home/xndadelin/Desktop/Scripts/steg/added.png')