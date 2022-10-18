from time import time
import cv2, pandas
import requests
from datetime import datetime

first_frame = None
df=pandas.DataFrame(columns=["Date","Time"])

video = cv2.VideoCapture(0)
print('')

class send_payload:
    def __init__(self):
        self.payload_insert = {"id":'',"date_time":''}

obj_send_payload = send_payload()
while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status=1
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    print(status)

    if status == 1:
        current_dateTime = datetime.now()
        #format the 12 hr format
        d = datetime.strptime(str(current_dateTime.hour)+":"+str(current_dateTime.minute), "%H:%M")
        formatted_time = d.strftime("%I:%M %p")
        #format the current date in words 
        formatted_date = datetime.now().strftime("%B %d, %Y")

        date_time = formatted_date + formatted_time
        obj_send_payload.payload_insert['date_time'] = str(date_time)
        check = requests.post('http://localhost:2022/connection',json=obj_send_payload.payload_insert)

        print(check.text)
        print("MOTION DETECTED!")
        print_pandas = df.append({"Date": formatted_date,"Time": formatted_time}, ignore_index=True)
        print(print_pandas)

    else:
        print("NO MOTION DETECTED!")

    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(1)

    if key == ord('c'):
        break


video.release()
cv2.destroyAllWindows