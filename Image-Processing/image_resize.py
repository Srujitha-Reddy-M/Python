import cv2

#input the path to your image
img = cv2.imread("galaxy.jpg",0)
print(img.shape)
print(img)
print(img.ndim)


r_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
#Original image
cv2.imshow("Galaxy",img)
#resized image
cv2.imshow("Galaxy",r_img)
cv2.imwrite("Galaxy_resized.jpg",r_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
