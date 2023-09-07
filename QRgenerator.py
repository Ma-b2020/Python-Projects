import qrcode

data=input("Enter the data to be embedded in the QRcode:-")

img = qrcode.make(data)
img.save("QRcode.jpg")
