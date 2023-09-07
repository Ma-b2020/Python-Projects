import qrcode

data = input("Enter the data to be embedded:-")

qr = qrcode.QRCode(version=2,box_size=10,border=5)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='grey',back_color='white')

img.save('MyQRCode.png')
