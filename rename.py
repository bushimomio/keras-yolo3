import os

a=os.listdir("VOCDevkit/VOC2007/Annotations")
b=os.listdir("VOCDevkit/VOC2007/JPEGImages")

for i in range(len(a)):
    os.rename("VOCDevkit/VOC2007/Annotations/{}".format(a[i]),"VOCDevkit/VOC2007/Annotations/{}.xml".format(str(i).zfill(3)))
    os.rename("VOCDevkit/VOC2007/JPEGImages/{}".format(b[i]),"VOCDevkit/VOC2007/JPEGImages/{}.jpg".format(str(i).zfill(3)))