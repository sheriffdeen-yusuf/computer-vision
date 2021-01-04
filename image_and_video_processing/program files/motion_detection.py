import cv2, time, pandas
from  datetime import  datetime


video = cv2.VideoCapture(0)

first_frame = None
status_list =[None, None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])

while True:

    check, frame = video.read()
    status = 0

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)


    if first_frame is None:
        first_frame = gray_frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 20, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # using value error(_,cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts, hierarchy = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("capurting", gray_frame)
    cv2.imshow("delta frame", delta_frame)
    cv2.imshow("threshold frame", thresh_frame)
    cv2.imshow("color frame", frame)

    key = cv2.waitKey(1)
    # print(gray_frame)
    # print(delta_frame)

    if key == ord('q'):
        if status==1:
            times.append(datetime.now())
        break



print(status_list)
print(times)

for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()