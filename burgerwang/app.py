import pymysql
from flask import Flask, render_template, session, request, redirect, url_for
from modelPembelian import Pembelian
from modelBarang import Barang
from modelPenjualan import Penjualan
from modelbuatakun import ModelSimpanUser
from models import Popupstore

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'

@app.route('/')
def index():
	if 'username' in session and session['admin'] == 'admin':
		username = session['username']
		return render_template('index.html', username = username)
	elif 'username' in session:
		username = session['username']
		return render_template('indexuser.html', username = username)
	return redirect(url_for('login'))
	# return render_template('halaman1.html')

# APP MENU #

@app.route('/MENU')
def MENU():
	return render_template('MENU.html')

# APP PEMBELIAN #

@app.route('/pembelian')
def pembelian():
    model = Pembelian()
    container = []
    container = model.selectDB()
    return render_template('pembelian.html', container=container)

@app.route('/insertPembelian', methods=['GET', 'POST'])
def insertPembelian():
	if request.method == 'POST':
		id_barang = request.form['id_barang']
		tgl_pembelian = request.form['tgl_pembelian']
		jumlah_pembelian = request.form['jumlah_pembelian']
		keterangan = request.form['keterangan']
		data = (id_barang, tgl_pembelian, jumlah_pembelian, keterangan)
		model = Pembelian()
		model.insertDB(data)
		return redirect(url_for('pembelian'))
	else:
		return render_template('insertPembelian.html')

@app.route('/updatePembelian/<id_pembelian>')
def updatePembelian(id_pembelian):
	model = Pembelian()
	data = model.getDBId_pembelian(id_pembelian)
	return render_template('updatePembelian.html', data= data)

@app.route('/update_processPembelian', methods=['GET', 'POST'])
def update_processPembelian():
    id_barang = request.form['id_barang']
    tgl_pembelian = request.form['tgl_pembelian']
    jumlah_pembelian = request.form['jumlah_pembelian']
    keterangan = request.form['keterangan']
    id_pembelian = request.form['id_pembelian']
    data = (id_barang, tgl_pembelian, jumlah_pembelian, keterangan, id_pembelian)
    model = Pembelian()
    model.updateDB(data)
    return redirect(url_for('pembelian'))

@app.route('/deletePembelian/<id_pembelian>')
def deletePembelian(id_pembelian):
	model = Pembelian()
	model.deleteDB(id_pembelian)
	return redirect(url_for('pembelian'))

# APP BARANG #

@app.route('/barang')
def barang():
    model = Barang()
    container = []
    container = model.selectDB()
    return render_template('barang.html', container=container)

@app.route('/insertBarang', methods=['GET', 'POST'])
def insertBarang():
	if request.method == 'POST':
		id_barang = request.form['id_barang']
		nama_barang = request.form['nama_barang']
		stock_barang = request.form['stock_barang']
		harga_beli = request.form['harga_beli']
		harga_jual = request.form['harga_jual']
		data = (id_barang, nama_barang, stock_barang, harga_beli, harga_jual)
		model = Barang()
		model.insertDB(data)
		return redirect(url_for('barang'))
	else:
		return render_template('insertBarang.html')

@app.route('/updateBarang/<id_barang>')
def updateBarang(id_barang):
	model = Barang()
	data = model.getDBbyid_barang(id_barang)
	return render_template('updateBarang.html', data=data)

@app.route('/update_processBarang', methods=['GET', 'POST'])
def update_processBarang():
	id_barang = request.form['id_barang']
	nama_barang = request.form['nama_barang']
	stock_barang = request.form['stock_barang']
	harga_beli = request.form['harga_beli']
	harga_jual = request.form['harga_jual']
	data = (nama_barang, stock_barang, harga_beli, harga_jual, id_barang)
	model = Barang()
	model.updateDB(data)
	return redirect(url_for('barang'))

@app.route('/deleteBarang/<id_barang>')
def deleteBarang(id_barang):
	model = Barang()
	model.deleteDB(id_barang)
	return redirect(url_for('barang'))

# APP PENJUALAN #

@app.route('/penjualan')
def penjualan():
	model = Penjualan()
	container = []
	container = model.selectDB()
	return render_template('penjualan.html', container=container)

@app.route('/insertPenjualan', methods=['GET', 'POST'])
def insertPenjualan():
	if request.method == 'POST':
		id_penjualan = request.form['id_penjualan']
		id_barang = request.form['id_barang']
		id_member = request.form['id_member']
		jumlah_penjualan = request.form['jumlah_penjualan']
		tgl_penjualan = request.form['tgl_penjualan']
		keterangan = request.form['keterangan']
		data = (id_penjualan, id_barang, id_member, jumlah_penjualan, tgl_penjualan, keterangan)
		model = Penjualan()
		model.insertDB(data)
		return redirect(url_for('penjualan'))
	else:
		return render_template('insertPenjualan.html')

@app.route('/updatePenjualan/<id_penjualan>')
def updatePenjualan(id_penjualan):
	model = Penjualan()
	data = model.getDBbyId_penjualan(id_penjualan)
	return render_template('updatePenjualan.html', data=data)

@app.route('/update_processPenjualan', methods=['GET', 'POST'])
def update_processPenjualan():
	id_penjualan = request.form['id_penjualan']
	id_barang = request.form['id_barang']
	id_member = request.form['id_member']
	jumlah_penjualan = request.form['jumlah_penjualan']
	tgl_penjualan = request.form['tgl_penjualan']
	keterangan = request.form['keterangan']
	data = (id_barang, id_member, jumlah_penjualan, tgl_penjualan, keterangan, id_penjualan)
	model = Penjualan()
	model.updateDB(data)
	return redirect(url_for('penjualan'))

@app.route('/deletePenjualan/<id_penjualan>')
def deletePenjualan(id_penjualan):
	model = Penjualan()
	model.deleteDB(id_penjualan)
	return redirect(url_for('penjualan'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pengguna = Popupstore(username, password)
        if pengguna.authenticate():
            session['username'] = username
            session['admin'] = pengguna.accountType()
            return redirect(url_for('index'))
        msg = 'Salah!'
        return render_template('login.html', msg = msg)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', '')
    return redirect(url_for('index'))

@app.route('/buat_akun', methods = ['GET', 'POST'])
def buat_akun():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nama = request.form['nama']
        tanggal_lahir = request.form['tanggal_lahir']
        jenis_kelamin = request.form['jenis_kelamin']
        no_telp = request.form['no_telp']
        alamat = request.form['alamat']
        data = (username, password, nama, tanggal_lahir, jenis_kelamin, no_telp, alamat)
        model = ModelSimpanUser()
        model.insertDB(data)
        return redirect(url_for('login'))
    else:
        return render_template('buat_akun.html')

if __name__ == '__main__':
    app.run(debug = True)