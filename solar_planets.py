import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Mercury",(40,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Venus",(60,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Earth",(80,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Mars",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Jupiter",(120,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Saturn",(220,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Uranus",(270,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))
cv2.putText(img,"Neptune",(300,300),cv2.FONT_HERSHEY_COMPLEX,0.5, (255,255,255))


cv2.imshow("output",img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)



