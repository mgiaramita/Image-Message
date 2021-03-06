# Image-Message
Custom LSD (Least Significant Digit) Steganography algorithm that can encode 1 character per pixel.

<B>How:</B>
  
    pixel data: (Red, Green, Blue) values 0-255
  
    character: int value 0-255
  
    char 'f' has an ascii value of 102
  
    If the pixel we want to encode this char in has the RGB values (156, 222, 000)
  
    Split 102 into three seperate digits 1  0  2. 
    
    Replace the least significant digit in the respective color channel with these values.
  
   So we end up with a new pixel containing the values (15<B>1</B>, 22<B>0</B>, 00<B>2</B>)
   
<B>Usage:<B>

    ImageMessage.py -e [imagename] [message.txt]  (encode message)
    
    ImageMessage.py -d [imagename] [output.txt]   (decode message)
               

#Example

Original Image (400x400)

![Alt Text](https://github.com/mgiaramita/Image-Message/blob/master/imgs/mona.jpg)

Output containing the entirety of Shakespeare's Romeo and Juliet

![Alt Text](https://github.com/mgiaramita/Image-Message/blob/master/imgs/out.png)
