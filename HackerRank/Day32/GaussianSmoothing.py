#Python PIL | GaussianBlur() method


# Importing Image and ImageFilter module from PIL package 
#radius:radius value used here is 5.
from PIL import Image, ImageFilter 

# creating a image object 
im1 = Image.open(r"C:\Users\System-Pc\Desktop\leave.JPG") 

# applying the Gaussian Blur filter 
im2 = im1.filter(ImageFilter.GaussianBlur(radius = 5)) 

im2.show() 

#radius:radius value used here is 2.
Importing Image and ImageFilter module from PIL package 
from PIL import Image, ImageFilter 

# creating a image object 
im1 = Image.open(r"C:\Users\System-Pc\Desktop\leave.JPG") 

# applying the Gaussian Blur filter 
im2 = im1.filter(ImageFilter.GaussianBlur(radius = 2)) 

im2.show() 

#Apply a Gauss filter to an image with Python
# ImageFilter for using filter() function 
from PIL import Image, ImageFilter 

# Opening the image 
# (R prefixed to string in order to deal with '\' in paths) 
image = Image.open(r"IMAGE_PATH") 

# Blurring image by sending the ImageFilter. 
# GaussianBlur predefined kernel argument 
image = image.filter(ImageFilter.GaussianBlur) 

# Displaying the image 
image.show()

#Blurring a small region in an image:
from PIL import Image, ImageFilter 

image = Image.open(r"FILE_PATH") 

# Cropping the image 
smol_image = image.crop((0, 0, 150, 150)) 

# Blurring on the cropped image 
blurred_image = smol_image.filter(ImageFilter.GaussianBlur) 

# Pasting the blurred image on the original image 
image.paste(blurred_image, (0,0)) 

# Displaying the image 
image.save('output.png') 
