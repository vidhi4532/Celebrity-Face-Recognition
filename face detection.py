import os
import cv2
import numpy

face_cascade_alt = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
face_cascade_default=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade_alt2=cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
face_cascade_alt_tree=cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml')
face_cascade_cat=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
face_cascade_ext=cv2.CascadeClassifier('haarcascade_frontalface_extended.xml')
path=os.path.join("channing tatum")
list=os.listdir(path)
list1=sorted(list)
print(list1)
err=[]
for img in list1:
    try:
        img_path = os.path.join("channing tatum",img)
        image=cv2.imread(img_path,1)
        # print(os.path.join(path,img))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('face',gray)
        #cv2.waitkey
        profiles = profile_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)
        if profiles==():
            profiles=face_cascade_alt.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)
        if profiles==():
            profiles=face_cascade_alt2.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)
        if profiles==():
            profiles=face_cascade_alt_tree.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)
        if profiles==():
            profiles=face_cascade_ext.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)
        if profiles==():
             profiles=face_cascade_cat.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)
        if profiles==():
             profiles=face_cascade_default.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=3)
        for (x,y,w,h) in profiles:
            #cv2.rectangle(image,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
            face=image[y:y+h+10,x:x+w]
            cv2.imshow('face',face)
            cv2.waitKey(3)
            cv2.imwrite(os.path.join(img),face)
    except:
        err.append(img)
        continue


print(err)
