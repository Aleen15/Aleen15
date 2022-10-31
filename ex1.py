import cv2 #library import
img=cv2.imread("sample 1.jpg") #read image
cv2.imwrite("copy.png",img) #save as image
print(img.shape)
print(img.size)
print(img.dtype)
cv2.imshow("AI_MSTER",img)
cv2.waitKey(0)
cv2.destroyAllwindows()
