from PIL import Image, ImageDraw, ImageFont
import os
import random

#Opening the blank page
page = Image.open("page.jpeg")

#Getting the pixel width and height of the page
width, height = page.size

#Making a copy of the blank page
copy = page.copy()

#Making ImageDraw object to add text to it
draw = ImageDraw.Draw(copy)

#Location of fonts folder
fonts_folder = "C:\\Users\\troge\\Desktop\\tempfont\\fonts"
#Making ImageFont object of users font
myfont = ImageFont.truetype(os.path.join(fonts_folder,"icomoon.ttf"), 64)

'''print("Enter Text that you want on the paper")'''

text = """There are several schools of thought on how a person should start learning to program. One school of thought is that a lower-level programming language such as Assembly or C are the most appropriate languages to start with because they force new developers to write their own data structures, learn about pointers and generally work their way through the hard problems in computer science.\nThere's certainly wisdom in this "low-level first" philosophy because it forces a beginner to gain a strong foundation before moving on to higher level topics such as web and mobile application development. This philosophy is the one most commonly used in university computer science programs."""

#calculated pixels by measuring cm value of individual items and relating it with the pixels from the size of the page.jpg
left_margin = 440
top_margin = 350
line_space = 96

#start_index = 0
space = text.index(" ")
lwidth = 0

for index, letter in enumerate(text):
    '''if(letter == " "):
                    #letter = "  "
                    space = index'''
    if((letter == "\n") or (lwidth >= (width-left_margin-100))):
        #start_index = index
        lwidth = 0
        top_margin += line_space
    human = random.randint(0,5)
    add_sub = random.randint(0,1)
    if(add_sub == 0):
        draw.text((left_margin+lwidth,top_margin+human), letter, fill = (0,15,85,255), font = myfont)
    else:
        draw.text((left_margin+lwidth,top_margin-human), letter, fill = (0,15,85,255), font = myfont)
    lwidth += draw.textsize(letter, myfont)[0]

copy.save('text.png')
#Getting the width and height of the text
'''total_text_width, text_height = draw.textsize(text, myfont)

left_margin = 440

top_margin = 350

line_space = 97

for index,letter in enumerate(text):
    if(letter == " "):
        if(draw.textsize(text[:index+1], myfont)[0]>=)
'''



'''linewidth = 0

leftmar = 440

topmar = 350

line_space = 100

for word in text.split():
    wwidth, wheight = draw.textsize(word, myfont)
    print(word)
    print(linewidth)
    print(wwidth)
    print(topmar)
    if((linewidth + wwidth) >= width):
        topmar+=line_space
    draw.text((linewidth+leftmar,topmar), word+" ", fill = (0,15,85,255), font = myfont)
    linewidth+=wwidth
    linewidth+=draw.textsize(" ", myfont)[0]'''

'''    print(word)
    lwidth, lheight = draw.textsize(text[:text.index(word)], myfont)
    print(lwidth)
    if(lwidth >= (width-500)):
        break
    else:
        draw.text((440+lwidth,350), word, fill = (0,15,85,255), font = myfont)'''
'''draw.text((440,350+100), text[text.index(word):], fill = (0,15,85,255), font = myfont)'''



'''from PIL import Image, ImageDraw, ImageFont

import os

img = Image.new('RGBA',(1000,1000),'white')

draw = ImageDraw.Draw(img)

fontsFolder = "C:\\Users\\troge\\Desktop\\Font20\\fonts"

myfont = ImageFont.truetype(os.path.join(fontsFolder,"icomoon.ttf"), 32)

text = "Hello There General Kenobi"

print(draw.textsize(text, myfont))

draw.text((20,150), text, fill = "blue", font = myfont)

img.save('text.png')
'''
