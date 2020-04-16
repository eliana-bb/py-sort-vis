from PIL import Image
from PIL import ImageDraw
import PIL
from huergb import hue

Width = 1920
Height = 1080

def sortImage(importarray, importname):
    array = importarray
    name = importname
    #print("Started rendering " + str(name))
    img = Image.new("RGB" , (Width , Height) , color=(40,40,40))
    pixels = img.load()

    columnWidth = Width/len(array)
    heightUnit = Height/len(array)

    draw = ImageDraw.Draw(img)

    # print(str(columnWidth) + " , " + str(heightUnit))

    for i in range(len(array)):
        #print("step1")
        draw.rectangle([int(round(i*columnWidth)), int(round(Height-(array[i]+1)*heightUnit)), int(round((i+1)*columnWidth-1)), Height], fill=hue(int(round(array[i]*(1530)/len(array))) + 1))
        #for w in range(int(round(i*columnWidth)), int(round((i+1)*columnWidth-1))): #for this column:
        #    for h in range(int(round(1080-(array[i]+1)*heightUnit)), 1080): #from the relevant point down:
        #        pixels[w,h] = hue(int(round(array[i]*(1530)/len(array))) + 1)
                #print(str(w) + " , " + str(h) + " , " + str(i) + " , " + str(array[i]))
    
    img.save("./imgs/"+ str(name) + ".png", format="PNG")
    print("Rendered Frame " + str(name))