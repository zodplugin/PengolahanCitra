import cv2
import numpy as np
import matplotlib.pyplot as plt  


img1 = cv2.imread('a.png')
img2 = cv2.imread('b.png')
dest_or = cv2.bitwise_or(img1,img2,mask=None)
dest_xor = cv2.bitwise_xor(img1,img2,mask=None)
dest_and = cv2.bitwise_and(img1,img2,mask=None)
dest_nand = cv2.bitwise_not(cv2.bitwise_and(img1,img2,mask=None),mask=None)
dest_nor = cv2.bitwise_not(cv2.bitwise_or(img1,img2,mask=None),mask=None)
dest_xnor = cv2.bitwise_not(dest_xor,mask=None)
dest_add = cv2.add(img1,img2,mask=None)
dest_sub = cv2.subtract(img1,img2,mask=None)
dest_mul = cv2.multiply(img1,img2)


image = np.concatenate((cv2.putText(dest_or,"Operation OR",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1),(cv2.putText(dest_xor,"Operation XOR",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)),(cv2.putText(dest_and,"Operation AND",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)),(cv2.putText(dest_nand,"Operation NAND",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)),(cv2.putText(dest_nor,"Operation NOR",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)),(cv2.putText(dest_xnor,"Operation XNOR",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)),(cv2.putText(dest_add,"Operation +",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)),(cv2.putText(dest_sub,"Operation -",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)),(cv2.putText(dest_mul,"Operation *",(40,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1))), axis=1)

cv2.imshow('Image',image)

cv2.waitKey(0)

