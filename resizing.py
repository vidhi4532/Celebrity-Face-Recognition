
import os
from PIL import Image
import cv2
#print(os.getcwd())
path=os.path.join("faces tom cruise")
#print(os.listdir())
files_list=os.listdir(path)
#print(len(files_list))
duplicates=[]
hash_keys={}
count=0
#print(files_list)
for f in files_list:
    path1=os.path.join("faces tom cruise",f)
    img=cv2.imread(path1,1)
    resized_image=cv2.resize(img,(256,256))
    #path2=os.path.join("resized paul walker")
    cv2.imwrite(f,resized_image)
#for  filename in files_list:
    #colorimg=cv2.imread(f"hello/paul walker/{filename}",1)
    #print(colorimg)
    #print(colorimg)
            #cv2.imshow('image',img)
            #cv2.waitKey(0)
    
    #new_height=1000
    #new_width=1000
    #img=cv2.resize(colorimg,(new_width,new_height))
    #print(img)
    #ext='jpg'
    #open(f"{count}.{ext}",'wb').write(img.content)
    #count+=1


