#Python PIL | MedianFilter() and ModeFilter() method
# Importing Image and ImageFilter module from PIL package 
from PIL import Image, ImageFilter 
	
# creating a image object 
im1 = Image.open(r"C:\Users\sadow984\Desktop\download2.JPG") 
	
# applying the median filter 
im2 = im1.filter(ImageFilter.MedianFilter(size = 3)) 
	
im2.show() 


#Python | Bilateral Filtering
import cv2 

# Read the image. 
img = cv2.imread('taj.jpg') 

# Apply bilateral filter with d = 15, 
# sigmaColor = sigmaSpace = 75. 
bilateral = cv2.bilateralFilter(img, 15, 75, 75) 

# Save the output. 
cv2.imwrite('taj_bilateral.jpg', bilateral) 
