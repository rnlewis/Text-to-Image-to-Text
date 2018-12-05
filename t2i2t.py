from PIL import Image
from os import *

#Author: R. Nathan Lewis
#Date: 12/4/18

chdir(__file__.replace(path.basename(__file__),''))

#Converts string into ASCII byte
def str2bin(str):
    bi = ''
    for i in str:
        #chr to ascii
        a = bin(ord(i))[2:]
        #add 0's before ascii to make str length = 8
        z = '0'*(8-len(a))
        #append bin to str
        bi = bi+z+a
    return bi
    
#Converts binary string to ASCII characters
def bin2str(bi):
    str = ''
    #for every set of 8 binary numbers
    for i in range(len(bi)//8):
        #get number string
        s = bi[i*8:i*8+8]
        #append chr to str
        str = str+chr(int(s,2))
    return str

#Converts string of ASCII characters into hex image format
def str2img(str,size=16):
    line = str2bin(str)
    h = hex(int(line,2))[2:]
    while len(h)%6 != 0:
        h = h + '00'
        
    h1 = []

    for i in range(len(h)//6):
        h1.append(h[i*6:i*6+6])

    w = len(h1)*size
    h = size

    #Import Image
    img = Image.new('RGB',(w,h),(255,255,255))
    for i in range(len(h1)):
        col = Image.new('RGB',(size,size),'#'+h1[i])
        img.paste(col,(i*size,0))

    #Test Successful Conversion
    if str == img2str(img):
        print('Successful Encoding')
        direct = listdir()
        x = 0
        fn = 'color_img{}.png'.format(x)
        while fn in direct:
            x+=1
            fn = 'color_img{}.png'.format(x)
        img.save(fn)
        print('Image Saved to Local Directory: {}\{}'.format(getcwd(),fn))
        img.show()
    else:
        print('Something went wrong during Encoding. Please contact the author.')


#Converts linear Image PNG file to ASCII characters
def img2str(im):
    try:
        img = Image.open(im)
    except:
        img = im
    colors = []
    h = img.height
    for i in range(img.width//h):
        col = img.getpixel((i*h,0))
        colors.append(col)
    for i in range(len(colors)):
        col = list(colors[i])
        for j in range(len(col)):
            val = hex(col[j])[2:]
            if len(val)<2:
                val = val + '0'
            col[j] = val
        colors[i] = '{}{}{}'.format(col[0],col[1],col[2])
    while '00' in colors[len(colors)-1]:
        colors[len(colors)-1] = colors[len(colors)-1][:len(colors[len(colors)-1])-2]
    line = ''.join(colors)
    bi = '0'+bin(int(line,16))[2:]
    str = bin2str(bi)
    return str

