import PIL

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from IPython.display import display

image=Image.open("D:\Python Projects\Project_Data\Example.jfif")
image=image.convert('RGB')
images=[]

data=image.getdata()

intensity=0.1
intensity1=0.1
intensity2=0.1

text=[]

for i in range(0, 9):
    
        newdata=[]
        
        images.append(image.copy())
        
        if i in [0,1,2]:
            
            text.append('channel {} intensity {}'.format(0,intensity))
            
            for item in data:
                newdata.append((int(item[0]*intensity),item[1],item[2]))
        
            images[i].putdata(newdata)
            intensity+=0.4
            continue
            
        elif i in [3,4,5]:
            
            text.append('channel {} intensity {}'.format(1,intensity1))
            
            for item in data:
                
                newdata.append((item[0],int(item[1]*intensity1),item[2]))
                
            images[i].putdata(newdata)
            intensity1+=0.4
            continue
            
        elif i in [6,7,8]:
            
            text.append('channel {} intensity {}'.format(2,intensity2))
            
            for item in data:
                
                newdata.append((item[0],item[1],int(item[2]*intensity2)))
                
            images[i].putdata(newdata)
            intensity2+=0.4
            continue
            
first_image=images[0]

contact_sheet=PIL.Image.new(first_image.mode,(first_image.width*3,(first_image.height*3)+180))


display(contact_sheet)

x=0

y=0

for img in images:

     contact_sheet.paste(img,(x, y))

     if x+first_image.width == contact_sheet.width:
        
         x=0
         y=y+first_image.height+60
        
     else:
        
         x=x+first_image.width
    
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))

draw=ImageDraw.Draw(contact_sheet)

font=ImageFont.truetype('D:\Python Projects\Project_Data\Fanwood Text.ttf',30)

for n in range(0,9):
    
     if n in [0,1,2]:
            
         if n==0:
            
             pc=contact_sheet.getpixel((220,100))
             a=0
            
         elif n==1:
            
             pc=contact_sheet.getpixel((620,100))
             a=400
            
         elif n==2:
            
             pc=contact_sheet.getpixel((1020,100))
             a=800
            
         draw.text((a,225),font=font,text=text[n],fill=pc)

     if n in [3,4,5]:
        
         if n==3:
                
             pc=contact_sheet.getpixel((220,320))
             a=0
                
         elif n==4:
            
             pc=contact_sheet.getpixel((620,320))
             a=400
            
         elif n==5:
            
             pc=contact_sheet.getpixel((1020,320))
             a=800
            
         draw.text((a,480),font=font,text=text[n],fill=pc)
         a+=400
            
     if n in [6,7,8]:
        
         if n==6:
             pc=contact_sheet.getpixel((220,540))
             a=0
                
         elif n==7:
             pc=contact_sheet.getpixel((620,540))
             a=400
            
         elif n==8:
            
             pc=contact_sheet.getpixel((1020,540))
             a=800
            
         draw.text((a,735),font=font,text=text[n],fill=pc)
         a+=400
    
display(contact_sheet)
