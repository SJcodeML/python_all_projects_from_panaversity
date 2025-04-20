import qrcode 


# we are making qrcode and saving data into it then we'll save qrcode into file

# data= 'dont forget to subscribe'

# img = qrcode.make(data)

# img.save('C:/Users/HP/Desktop/qrcode/myqrcode.png')


# customization in qrcode

data= 'dont forget to subscribe'

qr= qrcode.QRCode(version = 1 , box_size=10 , border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color = 'red' , back_color = 'white')

img.save('C:/Users/HP/Desktop/qrcode/myqrcode1.png')

# for decoding(getting data from qrcode) we need python libraray 'pyzbar' we need to install pyzbar

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/HP/Desktop/qrcode/myqrcode1.png')

result = decode(img)

print(result)

#  OR   


# img = Image.open('C:/Users/HP/Desktop/qrcode/myqrcode1.png')  
# results = decode(img)  

# for result in results:  
#     print(result.data.decode('utf-8'))  # Output the decoded data  