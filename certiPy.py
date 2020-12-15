# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 05:47:22 2020
To automatically create receipts for conferences
Saves lots of manual time and typos, corrections

The template certificates are in image format
These are converted to PDF formats later

@author: Rahul Venugopal
"""
#%% Loading libraries
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

# Load the csv file with name list
participant_names = pd.read_csv('namelist.csv')

# Set the font type and size
font = ImageFont.truetype('PlayfairDisplay-Regular.ttf', 200)

for index,j in participant_names.iterrows():
    img = Image.open('certificate.jpeg')
    draw = ImageDraw.Draw(img)
    
    # Locate the x,y coordinate where you want the name to go
    draw.text(xy=(3065,2673),text='{}'.format(j['name']),fill=(0,0,0),font = font)
    img.save('pictures/{}.jpeg'.format(j['name']))
