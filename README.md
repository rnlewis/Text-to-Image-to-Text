# Text-to-Image-to-Text
Encodes strings of ASCII values to Image data and Decodes the Image data back into ASCII characters.

Requires PIL Python Image Library

Download files into New Folder as they will be working in this directory.

How it works:
  Encoding -- Text strings are manipulated in place into one string of binary data of their ASCII values.  The binary data is turned to hex which is separated into parts of 6, each set of 6 is used as the hex color value of each tile in order. A PNG image file is saved to the local directory.
  Decoding -- The image must be in the encoded format above.  Python will iterate through each tile and retrieve the color value in hex.  The hex list will be put together into a single string, transformed to binary, and separated into parts of 8.  These parts will each represent an ASCII character.  The original text will become evident.

Text strings must not include line breaks, as the program will be unable to encode any values beyond and including that point.
