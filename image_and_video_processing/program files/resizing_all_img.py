import cv2, glob

images = glob.glob('../images/*.jpg')
for image in images:
    img = cv2.imread(image, 0)
    resize_img = cv2.resize(img,(200, 200))
    cv2.imshow("hey see!",resize_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resize_" + image, resize_img)