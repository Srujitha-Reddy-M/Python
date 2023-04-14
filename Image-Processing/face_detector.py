import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#input the path for your image
img = cv2.imread("me.jpg")          
img = cv2.resize(img,(718,628))
g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
g_img = cv2.resize(g_img,(718,628))

face = face_cascade.detectMultiScale(g_img, scaleFactor = 1.08, minNeighbors=5)

for x,y,w,h in face:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)
print(type(face))
print(face)

cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
