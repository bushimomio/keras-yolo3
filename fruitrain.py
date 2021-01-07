import os
import random
import sys


a=os.listdir("VOCDevkit/VOC2007/JPEGImages")

for i in range(len(a)):
    a[i]=a[i].replace(".jpg","")

val=set(random.sample(a,int(len(a)*float(sys.argv[1]))))
b=set(a)-val
train=set(random.sample(b,int(len(a)*float(sys.argv[2]))))
test=set(a)-val-train

for i,j in {"val.txt":val,"train.txt":train,"test.txt":test}.items():
    with open(i,"w") as f:
        for k in j:
            f.write("{}\n".format(k))





