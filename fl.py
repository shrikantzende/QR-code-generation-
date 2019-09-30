from flask import *
import qrcode
from PIL import Image
app = Flask(__name__)
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5

	)
@app.route('/')
def ram():
	return render_template("login.html ")
@app.route('/da',methods=['GET','POST'])
def shri():
	import os
	data=request.form.get('name')
	da=request.form.get('email')
	tt=request.form.get('address')
	z=  data +"\n"+ da + "\n" + tt

	qr.add_data(z)
	qr.make(fit=True)
	img=qr.make_image(fill="black",back_color="white")
	# os.remove('static/aaa.png')
	import random
	z=random.randint(0,100)
	img.save("static/"+str(z)+".png")
	return render_template("index.html",z=str(z))


if __name__ == "__main__":
    app.run()