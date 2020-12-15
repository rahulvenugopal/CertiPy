# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 05:47:22 2020
To automatically add name to certificate template for conferences
Saves lots of manual time and typos, corrections

The template certificates are in image format
There is a csv file called namelist containing names

@author: Rahul Venugopal
"""
#%% Loading libraries
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load the csv file with name list
participant_names = pd.read_csv('namelist.csv')

# Set the font type and size | Install the font if not there
font = ImageFont.truetype('arial.ttf', 60)

for index,j in participant_names.iterrows():
    
    # Open the original template image
    img = Image.open('template.jpg')
    draw = ImageDraw.Draw(img)
    
    # Locate the x,y coordinate where you want the name to go
    # This can be done by opening the image in paint and look up bottom left
    # area to see the xy loc
    
    # Grabbing each row in a loop
    name_to_add = '{}'.format(j['name'])
    # Each name will have its own lenght (width,w) and height (depends on font,h)
    w, h = draw.textsize(name_to_add)
    
    # Top left corner of the text is xy location
    # y location will be fixed, but x loc should change based on length of text
    # Change the color of text using fill argument
    draw.text(xy = (1200-(3*w),750),text = name_to_add,
              fill=(0,102,178),font = font)
    
    # Saving the image
    # You can change the format to PDf by replacing jpg
    img.save('certificate_generated/{}.jpg'.format(j['name']))
