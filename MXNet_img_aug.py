import d2lzh as d2l
import mxnet as mx
from mxnet import autograd, gluon, image, init, nd
from mxnet.gluon import data as gdata, loss as gloss, utils as gutils
import sys
import time
import matplotlib.pyplot as plt
import os

# d2l.set_figsize()
# img = image.imread('data/44.jpg')
# # d2l.plt.imshow(img.asnumpy())
#
# # def apply(img, aug, num_rows=2, num_cols=4, scale=1.5):
# #     Y = [aug(img) for _ in range(num_rows * num_cols)]
# #     d2l.show_images(Y, num_rows, num_cols, scale)
# #
# # apply(img, gdata.vision.transforms.RandomFlipLeftRight())
# # plt.show()
#
# fimg = gdata.vision.transforms.RandomFlipLeftRight()(img)
# # print(fimg)
# # print(type(img))
#
# d2l.plt.imshow(fimg.asnumpy())
# d2l.plt.imsave("data/qswqsqws.jpg",fimg.asnumpy())
# plt.show()
#
def get_img_list(path):
    img_list = []
    files = os.listdir(path)
    for f in files:
        if os.path.splitext(f)[1] == ".jpg" or os.path.splitext(f)[1] == ".png":
            img_list.append(os.path.join(path,f))
    return img_list

def main(path):
    img_list = get_img_list(path)
    for n,i in enumerate(img_list):
        flip_left_right_img = gdata.vision.transforms.RandomFlipLeftRight()(image.imread(i))
        d2l.plt.imsave("data/{}_flip_left_right_img.jpg".format(n), flip_left_right_img.asnumpy())

        flip_top_bottom_img = gdata.vision.transforms.RandomFlipTopBottom()(image.imread(i))
        d2l.plt.imsave("data/{}_flip_top_bottom_img.jpg".format(n), flip_top_bottom_img.asnumpy())

        brightness_img = gdata.vision.transforms.RandomBrightness(0.5)(image.imread(i))
        d2l.plt.imsave("data/{}_brightness_img.jpg".format(n), brightness_img.asnumpy())

        hue_img = gdata.vision.transforms.RandomHue(0.5)(image.imread(i))
        d2l.plt.imsave("data/{}_hue_img.jpg".format(n), hue_img.asnumpy())

        jitter_img = gdata.vision.transforms.RandomColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5)(image.imread(i))
        d2l.plt.imsave("data/{}_jitter_img.jpg".format(n), jitter_img.asnumpy())

        saturation_img = gdata.vision.transforms.RandomSaturation(0.5)(image.imread(i))
        d2l.plt.imsave("data/{}_saturation_img.jpg".format(n), saturation_img.asnumpy())
        
        shape_aug = gdata.vision.transforms.RandomResizedCrop((512, 512), scale=(0.1, 1), ratio=(0.5, 2))(i)
        d2l.plt.imsave("data/{}_shape_aug_img.jpg".format(n), shape_aug.asnumpy())

if __name__ == '__main__':
    path = r"E:\Pycharm\MXNet\MXNet_ligong\data"
    main(path)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # apply(img, gdata.vision.transforms.RandomFlipTopBottom())
#
