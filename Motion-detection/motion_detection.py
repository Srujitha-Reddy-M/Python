import cv2, time
from datetime import datetime
import pandas as pd

first_frame = None
s_list = [0,0]
time_list=[]
df = pd.DataFrame(columns=["Start_time","End_time"])

video = cv2.VideoCapture(0)
print("starting recording")

while True:
    check, frame = video.read()
    status =0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)          #converting to gray scale
    gray = cv2.GaussianBlur(gray,(21,21),0)                #apply gaussian blur to reduce noise and increase accuracy, 0 is std deviation

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    threshold_frame = cv2.threshold(delta_frame, 40, 255, cv2.THRESH_BINARY)[1]        #40 is taken as threshold based on the output difference array
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)                  #more the iterations better the result/smoother the image

    #findContours -we are passing 3 arguments: frame, function to remove external contours, builtin function used to approximte the contours
    (cnts,_) =cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 5000:
            continue
        status =1
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)

    s_list.append(status)

    s_list =s_list[-2:]
    if s_list[-1] != s_list[-2]:                                    #condition to check for change in status i.e.,when object enters or leaves the frame
        time_list.append(datetime.now())

    cv2.imshow("recording", frame)
    cv2.imshow("delta_frame",delta_frame)
    cv2.imshow("threshold frame",threshold_frame)

    key = cv2.waitKey(1)

    if key==ord('q'):
        if status==1:                                           #condition to note time when the object does not leave the frame before the video release
            time_list.append(datetime.now())
        break

print(s_list)
print(time_list)

#storing the timestamps when object enters and leaves into a pandas dataframe
for i in range(0,len(time_list),2):
    df=df.append({"Start_time":time_list[i],"End":time_list[i+1]},ignore_index=True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()
