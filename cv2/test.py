import cv2 as cv

filename="C:\\Users\\liuju\\Downloads\\111.png"
img=cv.imread(filename)
cv.imshow("Hello,Lenal",img)
cv.waitKey()
cv.destroyAllWindows()