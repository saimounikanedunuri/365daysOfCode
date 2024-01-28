Getting a Histogram of an Image
def main(): 
	try: 
		#Relative Path 
		img = Image.open("picture.jpg") 
		
		#Getting histogram of image 
		print img.histogram() 
		
	except IOError: 
		pass

if __name__ == "__main__": 
	main() 


Transposing an Image
	from PIL import Image 

def main(): 
	try: 
		#Relative Path 
		img = Image.open("picture.jpg") 
		
		#transposing image 
		transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT) 
		
		#Save transposed image 
		transposed_img.save("transposed.jpg") 
	except IOError: 
		pass

if __name__ == "__main__": 
	main() 


Split an image into individual bands
from PIL import Image 

def main(): 
	try: 
		#Relative Path 
		img = Image.open("picture.jpg") 
		
		#splitting the image 
		print img.split() 
	except IOError: 
		pass

if __name__ == "__main__": 
	main() 
