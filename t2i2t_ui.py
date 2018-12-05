from os import *
from t2i2t import *

#Author: R. Nathan Lewis
#Date: 12/4/18

print('Welcome to Text to Image to Text!\n')
chdir(__file__.replace(path.basename(__file__),''))

      
def encode():
    line = input('Write the text you wish to be Encoded:\n')
    if line != '':
        try:
            size = int(input('Color tile height in pixels (1,256; def:16): '))
            if size < 1 or size > 256:
                size = 16
        except:
            size = 16
        print('Tile Height: {}'.format(size))
        print('Generating Image...')
        str2img(line,size)
        print()
        __main__()
    else:
        print('Please use standard 7-bit ASCII characters\n')
        __main__()
    
def decode():
    print('Please choose a filename from {}:'.format(getcwd()))
    direct = listdir()
    num = 0
    for i in direct:
        if i.endswith('.png'):
            num+=1
            print(i)
    if num != 0:
        name = input('Filename: ')
        if name is not '':
            while name not in direct:
                print('That file was not found, please select an image from the list above.')
                name = input('Filename: ')
            img = '{}\{}'.format(getcwd(),name)
            print()
            print('Generating Text...')
            text = img2str(img)
            print(text)
            print()
            __main__()
        else:
            print()
            __main__()
    else:
        print('No valid files are found.\n')
        __main__()
    
def __main__():
    print('Would you like to Encode text to an image, or Decode an image from text?')
    option = 0
    while option not in ['1','2','3']:
        option = input('1 for Encode, 2 for Decode, 3 to Exit, and press Enter: ')
        print()
    if option is '1':
        encode()
    elif option is '2':
        decode()
    elif option is '3':
        print('Goodbye')
        exit()
    

__main__()
