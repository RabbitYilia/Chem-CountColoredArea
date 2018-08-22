from PIL import Image,ImageOps 
img=Image.open("demo.jpg")
total=0
global count
count=0

img_array=img.load()
width = img.size[0]  
height = img.size[1]  

def removeconner():
    width = img.size[0]  
    height = img.size[1]
    for y in range(0, 400):
        for x in range(0, 400):
            img_array[x,y]=(0,0,0)
            img_array[width-x-1,height-y-1]=(0,0,0)
            img_array[x,height-y-1]=(0,0,0)
            img_array[width-x-1,y]=(0,0,0)

def removebarrier():
    width = img.size[0]  
    height = img.size[1]  
    for y in range(0, height):
        for x in range(0, width):
            thisr,thisg,thisb=img_array[x,y]
            img_array[x,y]=(0,0,0)
            if(thisr+thisg+thisb>100 and thisr+thisg+thisb<120):
                break

removeconner()
removebarrier()
img=ImageOps.mirror(img)
img_array=img.load()
removebarrier()
img=ImageOps.mirror(img)
img_array=img.load()
for x in range(0, width):
    for y in range(0, height):
        thisr,thisg,thisb=img_array[x,y]
        if(img_array[x,y]!=(0,0,0)):
            total=total+1
        if(img_array[x,y]==(0,0,255)):
            img_array[x,y]=(0,0,0)
        if(thisr-thisg>50):
            img_array[x,y]=(0,0,255)
            count=count+1

print count
print total
img.save("result.jpg")
