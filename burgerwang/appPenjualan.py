from flask import Flask, render_template, request, redirect, url_for
from models import Penjualan

app = Flask(__name__)

@app.route('/')
def index():
	model = Penjualan()
	container = []
	container = model.selectDB()
	return render_template('penjualan.html', container=container)

@app.route('/insert', methods=['GET', 'POST'])
def insert():
	id_barang = request.form['id_barang']
	id_member = request.form['id_member']
	jumlah_penjualan = request.form['jumlah_penjualan']
	tanggal_penjualan = request.form['tanggal_penjualan']
	keterangan = request.form['keterangan']
	data = (id_barang, id_member, jumlah_penjualan, tanggal_penjualan, keterangan)
	model = Penjualan()
	model.insertDB(data)
	return redirect(url_for('penjualan'))
else:
	return render_template('insertPenjualan.html')

@app.route('/update/<id_penjualan')
def update(id_penjualan):
	model = Penjualan()
	data = model.getDBbyId_penjualan(id_penjualan)
	return render_template('updatePenjualan.html', data=data)

@app.route('/update_process', methods=['GET', 'POST'])
def update_process():
	id_penjualan = request.form['id_penjualan']
	id_barang = request.form['id_barang']
	id_member = request.form['id_member']
	jumlah_penjualan = request.form['jumlah_penjualan']
	tanggal_penjualan = request.form['tanggal_penjualan']
	keterangan = request.form['keterangan']
	data = (id_barang, id_member, jumlah_penjualan, tanggal_penjualan, keterangan, id_penjualan)
	model = Penjualan()
	model.updateDB(data)
	return redirect(url_for('penjualan'))

@app.route('/delete/<id_penjualan>')
def delete(id_penjualan):
	model = Penjualan()
	model.deleteDB(id_penjualan)
	return redirect(url_for('penjualan'))

