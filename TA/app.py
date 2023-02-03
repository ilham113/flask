from flask import Flask, render_template, request, redirect, url_for, session
from models import Mproduk, Musername, Mcart
from werkzeug import secure_filename 
import os	

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/TA/static'
application.config['SECRET_KEY'] = '1234567890'
#satuan byte
application.config['MAX_CONTENT_PATH'] = 10000000


@application.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('login.html',)

@application.route('/daftarproduk', methods = ['GET', 'POST'])
def akun_saya():
	model = Mproduk()
	container = []
	container = model.selectDB()
	profil = identitas()
	if 'email' in session:
		email = session['email']
		return render_template('index.html', email=email, container=container)
	return redirect(url_for('login'))


@application.route('/admin', methods=['GET','POST'])
def admin():
	if 'email' in session :
		email = session['email']
		return render_template('admin.html', email=username)
	return redirect(url_for('login'))

@application.route('/akun_saya/identitas', methods = ['GET', 'POST'])
def identitas():
	model = Musername()
	container = []
	container = model.selectDB()
	return render_template('identitas.html', container=container)

@application.route('/akun_saya/identitas/update/<no>')
def updateuser(no):
	model = Musername()
	data = model.getDBbyNo(no)
	return render_template('update_akun.html',data=data)

@application.route('/akun_saya/identitas/update_process', methods=['GET', 'POST'])
def update_user_process():
	no = request.form['no']
	email = request.form['email']
	password = request.form['password']
	nama = request.form['nama']
	tanggal_lahir = request.form['tanggal_lahir']
	jenis_kelamin = request.form['jenis_kelamin']
	no_telp = request.form['no_telp']
	alamat = request.form['alamat']
	data = (email, password, nama, tanggal_lahir, no_telp, jenis_kelamin, alamat,no)
	model = Musername()
	model.updateDB(data)
	return redirect(url_for('identitas'))

@application.route('/admin/username/update/<no>')
def updateuseradmin(no):
	model = Musername()
	dataa = model.getDBbyNo(no)
	return render_template('update_akun_admin.html',dataa=dataa)

@application.route('/admin/username/update_user_process_admin', methods=['GET', 'POST'])
def update_user_process_admin():
	no = request.form['no']
	email = request.form['email']
	password = request.form['password']
	nama = request.form['nama']
	tanggal_lahir = request.form['tanggal_lahir']
	jenis_kelamin = request.form['jenis_kelamin']
	no_telp = request.form['no_telp']
	alamat = request.form['alamat']
	data = (email, password, nama, tanggal_lahir, jenis_kelamin, no_telp, alamat,no)
	model = Musername()	
	model.updateDB(data)
	return redirect(url_for('username'))


@application.route('/username')
def username():
	model = Musername()
	container = []
	container = model.selectDB()
	return render_template('username.html', container=container)

@application.route('/delete/<no>')
def deleteuser(no):
	model = Musername()
	model.deleteDB(no)
	return redirect(url_for('username'))

@application.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		#level = ['level']
		pengguna = Musername(email, password)
		if pengguna.authenticate() :
			session['email'] = email
			if session['email'] == 'admin@admin.com':
				return redirect(url_for('admin'))
			else :
				return redirect(url_for('akun_saya'))	
		msg = 'username/password salah'
		return render_template('login.html', msg=msg)
	return render_template('login.html')

@application.route('/logout')
def logout():
	session.pop('email', '')
	return redirect(url_for('login'))

@application.route('/buat_akun', methods = ['GET', 'POST'])
def buat_akun():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		nama = request.form['nama']
		tanggal_lahir = request.form['tanggal_lahir']
		jenis_kelamin = request.form['jenis_kelamin']
		no_telp = request.form['no_telp']
		alamat = request.form['alamat']
		data = (email, password, nama, tanggal_lahir, jenis_kelamin, no_telp, alamat)
		model = Musername()
		model.insertDB(data)
		return redirect(url_for('login'))
	else:
		return render_template('buat_akun.html')

@application.route('/buat_akun_admin', methods = ['GET', 'POST'])
def buat_akun_admin():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		nama = request.form['nama']
		tanggal_lahir = request.form['tanggal_lahir']
		jenis_kelamin = request.form['jenis_kelamin']
		no_telp = request.form['no_telp']
		alamat = request.form['alamat']
		data = (email, password, nama, tanggal_lahir, jenis_kelamin, no_telp, alamat)
		model = Musername()
		model.insertDB(data)
		return redirect(url_for('username'))
	else:
		return render_template('buat_akunadmin.html')
###########################################################################################
###########login###########################################################################


@application.route('/produk')
def produk():
	model = Mproduk()
	container = []
	container = model.selectDB()
	return render_template('produk.html', container=container )

@application.route('/insert', methods=['GET','POST'])
def insert():
	if request.method == 'POST':	
		nama_produk = request.form['nama_produk']
		g = request.files['gambar']
		filename = application.config['UPLOAD_FOLDER'] + '/' + secure_filename(g.filename)
		diskripsi = request.form['diskripsi']
		harga = request.form['harga']
		datap = (nama_produk, secure_filename(g.filename), diskripsi, harga)
		model = Mproduk()
		model.insertDB(datap)
		g.save(filename)
		return redirect(url_for('produk'))
	else:
		return render_template('insert_produk.html')

@application.route('/updateproduk/<no>')
def updateproduk(no):
	model = Mproduk()
	datap = model.getDBbyNo(no)
	return render_template('update_produk.html', datap=datap)

@application.route('/update_produk_process', methods=['GET','POST'])
def update_produk_process():
	no = request.form['no']
	nama_produk = request.form['nama_produk']
	g = request.files['gambar']
	filename = application.config['UPLOAD_FOLDER'] + '/' + secure_filename(g.filename)
	diskripsi = request.form['diskripsi']
	harga = request.form['harga']
	datap = (nama_produk, secure_filename(g.filename), diskripsi, harga,no)
	g.save(filename)
	model =Mproduk()
	model.updateDB(datap)
	return redirect(url_for('produk'))

@application.route('/deleteproduk/<no>')
def deleteproduk(no):
	model = Mproduk()
	model.deleteDB(no)
	return redirect(url_for('produk'))


########################################################

@application.route('/cart')
def cart():
	modelc = Mcart()
	container = []
	container = modelc.selectDB()
	return render_template('cart.html', container=container)

@application.route('/insertcartuser', methods=['GET','POST'])
def insertcartuser():
	modelE = Musername()
	model = Mproduk()
	containerE = []
	container = []
	containerE = modelE.selectDB()
	container = model.selectDB()
	if request.method == 'POST' :
		email = request.form['email']
		nama_produk = request.form['nama_produk']
		harga = int(request.form['harga'])
		jumlah = int(request.form['jumlah'])
		total = harga * jumlah
		datac = (email,nama_produk,harga,jumlah,total)
		model = Mcart()
		model.insertDB(datac)
		return redirect(url_for('index'))
	else:
		return render_template('insercart.html' ,container=container, containerE=containerE  )

@application.route('/insertcartadmin', methods=['GET','POST'])
def insertcartadmin():
	modelE = Musername()
	model = Mproduk()
	containerE = []
	container = []
	containerE = modelE.selectDB()
	container = model.selectDB()
	if request.method == 'POST' :
		email = request.form['email']
		nama_produk = request.form['nama_produk']
		harga = int(request.form['harga'])
		jumlah = int(request.form['jumlah'])
		total = harga * jumlah
		datac = (email,nama_produk,harga,jumlah,total)
		model = Mcart()
		model.insertDB(datac)
		return redirect(url_for('cart'))
	else:
		return render_template('insertcartadmin.html',container=container, containerE=containerE )


@application.route('/updatecartadmin', methods=['GET','POST'])
def updatecartadmin_process():
	modelE = Musername()
	model = Mproduk()
	containerE = []
	container = []
	containerE = modelE.selectDB()
	container = model.selectDB()
	if request.method == 'POST' :
		no = request.form['no']
		email = session['email']
		nama_produk = request.form['nama_produk']
		harga = int(request.form['harga'])
		jumlah = int(request.form['jumlah'])
		total = harga * jumlah
		datac = (email,nama_produk,harga,jumlah,total)
		model = Mcart()
		model.updateDB(datac)
		return render_template('cart', container=container, containerE=containerE)


@application.route('/updatecart/<no>')
def updatecart(no):
	modelE = Musername()
	model = Mproduk()
	containerE = []
	container = []
	containerE = modelE.selectDB()
	container = model.selectDB()
	model = Mcart()
	datac = model.getDBbyNo(no)
	return render_template('update_cart.html', datac=datac, container=container, containerE=containerE)

@application.route('/deletecart/<no>')
def deletecart(no):
	model = Mcart()
	model.deleteDB(no)
	return redirect(url_for('cart'))


###################################################################################



if __name__ == '__main__':
	application.run(debug=True)


