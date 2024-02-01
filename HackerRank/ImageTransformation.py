Below are image transformation techniques:
-----------------------------------------
Image Translation
Reflection 
Rotation
Scaling
Cropping
Shearing in x-axis
Shearing in y-axis

Image Translation:
------------------
import numpy as np
import cv2 as cv
img = cv.imread('girlImage.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()

Image Reflection:
-----------------
import numpy as np
import cv2 as cv
img = cv.imread('girlImage.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0, 0],
				[0, -1, rows],
				[0, 0, 1]])
reflected_img = cv.warpPerspective(img, M,
								(int(cols),
									int(rows)))
cv.imshow('img', reflected_img)
cv.imwrite('reflection_out.jpg', reflected_img)
cv.waitKey(0)
cv.destroyAllWindows()

Image Rotation:
---------------
import numpy as np
import cv2 as cv
img = cv.imread('girlImage.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
img_rotation = cv.warpAffine(img,
							cv.getRotationMatrix2D((cols/2, rows/2),
													30, 0.6),
							(cols, rows))
cv.imshow('img', img_rotation)
cv.imwrite('rotation_out.jpg', img_rotation)
cv.waitKey(0)
cv.destroyAllWindows()

Image Scaling:
-------------
import numpy as np
import cv2 as cv
img = cv.imread('girlImage.jpg', 0)
rows, cols = img.shape
img_shrinked = cv.resize(img, (250, 200),
						interpolation=cv.INTER_AREA)
cv.imshow('img', img_shrinked)
img_enlarged = cv.resize(img_shrinked, None,
						fx=1.5, fy=1.5,
						interpolation=cv.INTER_CUBIC)
cv.imshow('img', img_enlarged)
cv.waitKey(0)
cv.destroyAllWindows()

Image Cropping:
---------------
import numpy as np
import cv2 as cv
img = cv.imread('girlImage.jpg', 0)
cropped_img = img[100:300, 100:300]
cv.imwrite('cropped_out.jpg', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()

Image Shearing in X-Axis:
-------------------------
import numpy as np
import cv2 as cv
img = cv.imread('girlImage.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv.imshow('img', sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()

Image Shearing in Y-Axis:
-------------------------
import numpy as np
import cv2 as cv
img = cv.imread('girlImage.jpg', 0)
rows, cols = img.shape
M = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv.imshow('sheared_y-axis_out.jpg', sheared_img)
cv.waitKey(0)
cv.destroyAllWindows()
