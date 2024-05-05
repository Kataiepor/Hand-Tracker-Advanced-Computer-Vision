import cv2
import numpy as np

image = np.zeros ((512, 512, 3), np.uint8)

cv2.line(image, (0,0), (511, 511), (0, 255, 0), 5)

cv2.rectangle(image, (384, 0), (510, 128), (0, 0, 255), 5)

cv2.circle(image, (447, 63), 63, (255, 0, 0), -1)

cv2.imshow('Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

