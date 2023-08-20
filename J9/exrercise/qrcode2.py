# import pyqrcode
# from pyqrcode import QRCode
# qr = 'hyaghuobian85@gmail.com'
# new_qr = pyqrcode.create(qr)
# new_qr.svg('paython homa.svg')
# img = qr.make_image(
#     fill_color = "red",
#     back_color = "white")
# img.save("paython homa.svg")

import qrcode

img = qrcode.make('hyaghuobian85@gmail.com')
# img = img.make_image(fill_color = "red",back_color = "white")
img.save('paython homa.png')