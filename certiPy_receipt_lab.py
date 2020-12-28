# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 05:47:22 2020
To automatically add name, ID and number to receipt template for conferences
Saves lots of manual time and typos, corrections

The template is in image format
There is a csv file called namelist containing names, ID and number

@author: Rahul Venugopal
"""
#%% Loading libraries
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load the csv file with name list
participant_names = pd.read_csv('namelist.csv')

# Set the font type and size | Install the font if not there
font_for_name = ImageFont.truetype('timesbd.ttf', 30)
font_for_rest = ImageFont.truetype('times.ttf', 30)

for index,j in participant_names.iterrows():
    
    # Open the original template image
    img = Image.open('receipt.jpg')
    img = img.convert('RGB') # After an error
    draw = ImageDraw.Draw(img)
    
    # Locate the x,y coordinate where you want the name to go
    # This can be done by opening the image in paint and look up bottom left
    # area to see the xy loc
    
    # Grabbing each row in a loop
    name_to_add = '{}'.format(j['name'])
    
    # Top left corner of the text is xy location
    # y location will be fixed, but x loc should change based on length of text
    # Change the color of text using fill argument
    draw.text(xy = (776,525),text = name_to_add,
              fill=(0,0,0),font = font_for_name)
    
    ID_to_add = '{}'.format(j['ID'])
    draw.text(xy = (48,950),text = ID_to_add,fill=(0,0,0),font = font_for_rest)
    
    No_to_add = 'No.'+'{}'.format(j['No'])
    draw.text(xy = (48,386),text = No_to_add,fill=(0,0,0),font = font_for_rest)
    
    # Saving the image
    # You can change the format to PDf by replacing jpg
    img.save('receipt_generated/{}_Receipt.PDF'.format(j['ID']))
