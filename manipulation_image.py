import cv2

img=cv2.imread("assets/lena.jpg",1)
img=cv2.line(img,(0,255),(255,255),(18,155,182),30)
img=cv2.rectangle(img,(384,0),(510,128),(15,180,255),5)
img=cv2.circle(img,(447,63),63,(45,45,45),5)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("lena_copy.jpg",img=img)
    cv2.destroyAllWindows()
