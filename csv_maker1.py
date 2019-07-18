# -*- coding: utf-8 -*-
"""csv_maker.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S8Odio4iNUfB5JZxPgeGr4MgSTjougCh
"""

from PIL import Image
import cv2
import glob2
import pandas as pd
IMG_PATH = "/storage/research/Intern19_v2/DetectObjectsInVariedAndComplexImages/train_02/train_02"
ANOT_PATH = "anot_maker.csv"
LABEL_PATH = "class-descriptions-boxable.csv"
anot = pd.read_csv(ANOT_PATH)
labels = pd.read_csv(LABEL_PATH)

labels.columns = ["LabelName", "class"]

print("files loaded...")

import os, sys

path = "train_02/train_02/"
dirs = os.listdir( path )
final_size = 640;

def resize_aspect_fit():
    for item in dirs:
         if item == '.DS_Store':
             continue
         if os.path.isfile(path+item):
             im = Image.open(path+item)
             f, e = os.path.splitext(path+item)
             size = im.size
             ratio = float(final_size) / max(size)
             new_image_size = tuple([int(x*ratio) for x in size])
             im = im.resize(new_image_size, Image.ANTIALIAS)
             new_im = Image.new("RGB", (final_size,final_size))
             new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
             new_im.save(f + 'coco1.jpg', 'JPEG', quality=90)
resize_aspect_fit()

print("resized")
import time

IMG = glob2.glob(IMG_PATH+"/*.jpg")
print(IMG) 


def path_(text):
    return IMG_PATH+"/"+text+"coco1.jpg"



anot["ImageID"] = anot["ImageID"].apply(path_)
anot = anot.loc[anot['ImageID'].isin(IMG)]
anot = anot.dropna()


replacements = {l1: l2 for l1, l2 in zip(
    list(labels["LabelName"]), list(labels["class"]))}

anot = anot.replace(replacements)





anot = anot.rename(columns={"LabelName": "class"})

anot = anot[['ImageID', 'XMin', 'YMin', 'XMax', 'YMax', 'class']]


"""li = []
for image in IMG:
    im = Image.open(image)
    width,height=im.size
    tu = (image, height, width)
    print(tu)
    li.append(tu)"""

print("images loaded v2")

#imdet = pd.DataFrame(li)
#imdet.columns = ["ImageID", "h", "w"]

#mergedStuff = pd.merge(anot, imdet, on=['ImageID'], how='inner')
def inter(val):
	return int(round(val*640))
def inter_1(val):
	new=int(round(val*640))+1
	if new==641:
		return 640
	else:
		return new



anot["XMin"] = anot["XMin"].apply(inter)
anot["XMax"] = anot["XMax"].apply(inter_1)
anot["YMin"] = anot["YMin"].apply(inter)
anot["YMax"] = anot["YMax"].apply(inter_1)


#def int_(val):
# return int(val)


#mergedStuff["XMin"] = mergedStuff["XMin"].apply(int_)
#mergedStuff["XMax"] = mergedStuff["XMax"].apply(int_)
#mergedStuff["YMin"] = mergedStuff["YMin"].apply(int_)
#mergedStuff["YMax"] = mergedStuff["YMax"].apply(int_)

#dropper = ["h", "w"]
#new = mergedStuff.drop(dropper, axis=1)

class_ind = anot["class"]
class_ind = pd.DataFrame(class_ind)
class_ind = class_ind.drop_duplicates(subset=['class'])
class_ind["index"] = range(len(class_ind))


print(class_ind)
time.sleep(1)
class_ind.to_csv("classScript640.csv", index=False, header=False)
print(anot)
anot.to_csv("labelScript640.csv", index=False, header=False)

