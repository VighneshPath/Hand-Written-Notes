from PIL import Image, ImageDraw, ImageFont
import os
import random
import shelve

shelfFile = shelve.open("PageDim")

#Opening the blank page
page = Image.open("page.jpeg")

def convert_to_pixels(cm, multiplicative_factor):
    return cm*multiplicative_factor

#Getting the pixel width and height of the page
width, height = page.size

try:
    page_hor, page_ver, page_lmar, page_tmar, page_bmar, page_line_space = shelfFile["pagedimensions"]
except:
    print("Enter The following dimensions of the page in cm")
    print("Enter Horizontal Length of the Page")
    page_hor = round(float(input()))
    print("Enter Vertical Length of the Page")
    page_ver = round(float(input()))
    #Converting cm values to pixels
    horizontal_factor = width/page_hor
    vertical_factor = height/page_ver
    page_hor = width
    page_ver = height
    print("Enter Left Margin Length of the Page")
    page_lmar = float(input())
    page_lmar = round(convert_to_pixels(page_lmar, horizontal_factor))
    print("Enter Top Margin Length of the Page")
    page_tmar = float(input())
    page_tmar = round(convert_to_pixels(page_tmar, vertical_factor))
    print("Enter Bottom Margin Length of the Page")
    page_bmar = float(input())
    page_bmar = round(convert_to_pixels(page_bmar,vertical_factor))
    print("Enter Distance Between two horizontal lines on the page (rules)")
    page_line_space = float(input())
    page_line_space = round(convert_to_pixels(page_line_space, vertical_factor))

    #Page Size is stored in the format Page Horizontal, Page Vertical, Page Left Margin, Page Top Margin, Page Bottom Margin, Page Line Space
    shelfFile["pagedimensions"] = [page_hor, page_ver, page_lmar, page_tmar, page_bmar, page_line_space]


#Making a copy of the blank page
copy = page.copy()

#Making ImageDraw object to add text to it
draw = ImageDraw.Draw(copy)

'''#Location of fonts folder
fonts_folder = "C:\\Users\\troge\\Desktop\\tempfont\\fonts"'''
#Making ImageFont object of users font
myfont = ImageFont.truetype("icomoon.ttf", 64)

'''print("Enter Text that you want on the paper")'''
with open("writing_text.txt", "r") as f:
    text = f.read()

'''#calculated pixels by measuring cm value of individual items and relating it with the pixels from the size of the page.jpg
left_margin = 440
top_margin = 350
line_space = 96

#start_index = 0
space = text.index(" ")
lwidth = 0'''


page_no = 1
twidth = page_tmar
lwidth = 0

# page_hor, page_ver, page_lmar, page_tmar, page_bmar, page_line_space

page_lmar+=10
page_line_space -=2
image_list = []

for index, letter in enumerate(text):
    '''if(letter == " "):
                    #letter = "  "
                    space = index'''
    if((twidth+page_line_space >= page_ver - page_bmar) and lwidth >= (page_hor-page_lmar-100)):
        print("OK")
        print(page_no)
        print(twidth, page_ver-page_bmar)
        temp_copy = copy.convert("RGB")
        if(page_no == 1):
            first_image = temp_copy
        else:
            image_list.append(temp_copy)
        copy.save(f'text{page_no}.png')
        copy = page.copy()
        draw = ImageDraw.Draw(copy)
        lwidth = 0
        twidth = page_tmar
        page_no+=1
    '''if(twidth >= page_ver - page_bmar):
                    print(page_no)
                    print(twidth, page_ver-page_bmar)
                    copy.save(f'text{page_no}.png')
                    copy = page.copy()
                    draw = ImageDraw.Draw(copy)
                    lwidth = 0
                    twidth = page_tmar
                    page_no+=1'''
    if((letter == "\n") or (lwidth >= (page_hor-page_lmar-100))):
        #If there is no space to write characters
        #start_index = index
        lwidth = 0
        twidth += page_line_space
    human = random.randint(0,5)
    add_sub = random.randint(0,1)
    if(add_sub == 0):
        draw.text((page_lmar+lwidth,twidth+human), letter, fill = (0,15,85,255), font = myfont)
    else:
        draw.text((page_lmar+lwidth,twidth-human), letter, fill = (0,15,85,255), font = myfont)
    lwidth += draw.textsize(letter, myfont)[0]


    '''print(twidth, page_ver-page_bmar)'''

copy.save(f'text{page_no}.png')
copy.convert("RGB")
image_list.append(copy)
try:
    os.mkdir("MyPdf")
except FileExistsError:
    pass
first_image.save(r"MyPdf\assignment.pdf", save_all=True, append_images=image_list)

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
