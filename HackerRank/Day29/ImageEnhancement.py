Color Inversion using Pillow:
# Importing imagechops for using the invert() method
from PIL import Image, ImageChops

# Opening the test image, and saving it's object
img = Image.open('test.jpg')

# Passing the image object to invert() 
inv_img = ImageChops.invert(img)

# Displaying the output image
inv_img.show()


Wand sharpen() function – Python:
# Import library from Image 
from wand.image import Image

# Import the image
with Image(filename ='../geeksforgeeks.png') as image:
	# Clone the image in order to process
	with image.clone() as sharpen:
		# Invoke sharpen function with radius 50 and sigma 40
		sharpen.sharpen(50, 40)
		# Save the image
		sharpen.save(filename ='sharpen1.jpg')
