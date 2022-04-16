import cv2

cap=cv2.VideoCapture(0)
fourch=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter('output.avi',fourch,20.0,600,480)
while (cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)

        if (cv2.waitKey(1) & 0xFF==ord('q')):
            break
    else:
        break
out.release()
cap.release()