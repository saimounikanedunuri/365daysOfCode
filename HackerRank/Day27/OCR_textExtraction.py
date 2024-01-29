way-1: using 'pytesseract'

from PIL import Image 
from pytesseract import pytesseract 

# Defining paths to tesseract.exe 
# and the image we would be using 
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"csv\sample_text.png"

# Opening the image & storing it in an image object 
img = Image.open(image_path) 

# Providing the tesseract executable 
# location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract 

# Passing the image object to image_to_string() function 
# This function will extract the text from the image 
text = pytesseract.image_to_string(img) 

# Displaying the extracted text 
print(text[:-1])

way-2: using pillow
# Import Image for basic functionalities like open, save, show
# Import ImageDraw to convert image into editable format
# Import ImageFont to choose the font style
from PIL import Image, ImageDraw, ImageFont

# gfg_logo.jpeg image opened using open
# function and assigned to variable named img
img = Image.open('gfg_logo.jpeg')

# Image is converted into editable form using
# Draw function and assigned to d1
d1 = ImageDraw.Draw(img)

# Font selection from the downloaded file
myFont = ImageFont.truetype('/home/raghav/PycharmProjects/gfg/Mistral.ttf', 20)

# Decide the text location, color and font
d1.text((65, 10), "Sample text", fill =(255, 0, 0),font=myFont)

# show and save the image
img.show()
img.save("results.jpeg")

way-3: OCR on All the Images present in a Folder Simultaneously
# Python program to extract text from all the images in a folder 
# storing the text in corresponding files in a different folder 
from PIL import Image 
import pytesseract as pt 
import os 
	
def main(): 
	# path for the folder for getting the raw images 
	path ="E:\\GeeksforGeeks\\images"

	# path for the folder for getting the output 
	tempPath ="E:\\GeeksforGeeks\\textFiles"

	# iterating the images inside the folder 
	for imageName in os.listdir(path): 
			
		inputPath = os.path.join(path, imageName) 
		img = Image.open(inputPath) 

		# applying ocr using pytesseract for python 
		text = pt.image_to_string(img, lang ="eng") 

		# for removing the .jpg from the imagePath 
		imagePath = imagePath[0:-4] 

		fullTempPath = os.path.join(tempPath, 'time_'+imageName+".txt") 
		print(text) 

		# saving the text for every image in a separate .txt file 
		file1 = open(fullTempPath, "w") 
		file1.write(text) 
		file1.close() 

if __name__ == '__main__': 
	main() 
