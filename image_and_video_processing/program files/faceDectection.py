import cv2

face_cascade = cv2.CascadeClassifier("../haarcascade_frontalface_default.xml")


# image = cv2.imread("photo.jpg")
image = cv2.imread("six_face_new.jpg")  #while using this change the scalefactor to 1.1

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_dectect = face_cascade.detectMultiScale(gray_image, scaleFactor=1.03, minNeighbors=5)

for x,y,w,h in face_dectect:
    img = cv2.rectangle(image,(x,y), (x+w,y+h),(0,255,0),3)

print(type(face_dectect))
print(face_dectect)
resize_img = cv2.resize(image,(int(image.shape[1]/2),int(image.shape[0]/2)))
cv2.imshow('gray', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()