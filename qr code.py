import qrcode
from PIL import Image
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5

	)

data="hello Manish sir "
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("1.png")