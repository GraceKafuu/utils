from PIL import Image
import os

img_path = "image"
img_list = os.listdir(img_path)

for img in img_list:
	jpg_image_name = os.path.basename(img).split(".")[0]
	jpg_image = Image.open(img_path + "/" + img)
	jpg_image.thumbnail((512, 384), Image.ANTIALIAS)
	jpg_image.save("image_png/{}.png".format(jpg_image_name))
