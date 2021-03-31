import hashlib
import cv2
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import time
import numpy as np

from hashlib import md5
import os

os.chdir(r"C:\Users\arihant1199\Desktop\hello\channing tatum")
#print(os.getcwd())
#print(os.listdir())
files_list=os.listdir()
#print(len(files_list))
duplicates=[]
hash_keys={}
for index, filename in enumerate(os.listdir()):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash=hashlib.md5(f.read()).hexdigest()
            img= cv2.imread(filename)
            #cv2.imshow('image',img)
            #cv2.waitKey(0)
            #new_height=1000
            #new_width=1000

        
            #print(filehash)
        if filehash not in hash_keys:
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))
print(duplicates)
for index in duplicates:
    os.remove(files_list[index[0]])