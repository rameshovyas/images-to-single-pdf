# Ramesh Vyas
# Python script to merge all images in a folder in a single pdf file

import os
import subprocess
from fpdf import FPDF
from PIL import Image

rootdir = os.getcwd()
count=0
imagelist = []

# Allowed image formats
ext = [".png", ".jpg",".jpeg"]
print ("Started creating document " + " in directory : " + rootdir)
for subdir, dirs, files in os.walk(rootdir):
  for filename in sorted(files):    
    if filename.endswith(tuple(ext)):            
      imagelist.append(filename)
      
pdf = FPDF()

for imageFile in imagelist:    
    
    cover = Image.open(imageFile)
    width, height = cover.size
    # Pixel to mm conversion (1px=0.264583 mm)
    width, height = float(width * 0.264583), float(height * 0.264583)

    # Using A4 format size 
    pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

    # get page orientation from image size 
    orientation = 'P' if width < height else 'L'

    #  Confirm image size does not exceed the pdf format size
    width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
    height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

    pdf.add_page(orientation=orientation)
    
    pdf.image(imageFile, 0, 0, width, height)

    
#Final output in compiled.pdf    
pdf.output("compiled.pdf", "F")
print ("Completed merging " + " in directory : " + rootdir)
