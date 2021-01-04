import cv2, time

video = cv2.VideoCapture(0)

number_of_iteration = 0
while True:
    number_of_iteration += 1
    check, frame = video.read()

    print(check)
    print(frame)
    gray_color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # time.sleep(4)
    cv2.imshow("capurting", gray_color)

    # cv2.waitKey(0) any key u press will terminate the process
    key =  cv2.waitKey(1) #1 milli second

    if key == ord('q'):
        break

print(number_of_iteration)
video.release()
cv2.destroyAllWindows()