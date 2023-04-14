import cv2, time

video = cv2.VideoCapture(0)
a=0
print("starting recording")
while True:
    a+=1
    check, frame = video.read()
    # print(check)
    #print(frame)
    cv2.imshow("recording", frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
