Cropping an Image: 
Image.crop(box) takes a 4-tuple (left, upper, right, lower) pixel coordinate, and returns a rectangular region from the used image.

from PIL import Image 

def main(): 
	try: 
		#Relative Path 
		img = Image.open("picture.jpg") 
		width, height = img.size 
		
		area = (0, 0, width/2, height/2) 
		img = img.crop(area) 
		
		#Saved in the same relative location 
		img.save("cropped_picture.jpg") 
		
	except IOError: 
		pass

if __name__ == "__main__": 
	main() 


Resizing an Image:
Image.resize(size)- Here size is provided as a 2-tuple width and height
from PIL import Image 

def main(): 
	try: 
		#Relative Path 
		img = Image.open("picture.jpg") 
		width, height = img.size 

		img = img.resize((width/2, height/2)) 
		
		#Saved in the same relative location 
		img.save("resized_picture.jpg") 
	except IOError: 
		pass

if __name__ == "__main__": 
	main() 


Pasting an image on another image: 
The second argument can be a 2-tuple (specifying the top left corner), or a 4-tuple (left, upper, right, lower) – in this case the size of pasted image must match the size of this box region, or None which is equivalent to (0, 0).
from PIL import Image 

def main(): 
	try: 
		#Relative Path 
		#Image on which we want to paste 
		img = Image.open("picture.jpg") 
		
		#Relative Path 
		#Image which we want to paste 
		img2 = Image.open("picture2.jpg") 
		img.paste(img2, (50, 50)) 
		
		#Saved in the same relative location 
		img.save("pasted_picture.jpg") 
		
	except IOError: 
		pass

if __name__ == "__main__": 
	main() 

##An additional argument for an optional image mask image is also available. 
