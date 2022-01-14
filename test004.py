import qrcode
from PIL import Image

print("This program generates a qr code linked to my resume")

img = qrcode.make('https://docs.google.com/document/d/1l-FzlHGT8-8gEK-JNbfKXapWt1mJNToC/edit?usp=sharing&ouid=113545058400243131395&rtpof=true&sd=true')
img.save('C:/Python/pyImages/resumeQr.jpg')
img.show()
print("Image is saved")