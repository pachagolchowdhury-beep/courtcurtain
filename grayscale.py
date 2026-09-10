import cv2

image = cv2.imread(r"C:\Users\BISWAS\Downloads\snake/projapoti.jpeg")

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', gray_img)


cv2.waitKey(0)


cv2.destroyAllWindows()
