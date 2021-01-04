import cv2

img = cv2.imread('two_face.jpg', 1)
print(img)
print(img.shape)

resize_img = cv2.resize(img,(700,800))
cv2.imwrite("two_face_new.jpg", resize_img)
cv2.imshow('dubai_pix', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()