from flask import Flask, render_template, request, redirect, url_for
from models import Pembelian

aplication = Flaks(__name__)

@aplication.route('/')
def index():
	model = Pembelian()
	container = []
	container = model.selectDB()
	return render_template('pembelian.html', container=container)

@aplication.route('/insert', methods=['GET', 'POST'])
def insert():
	if request.method == 'POST':
		id_barang = request.form['id_barang']
		tgl_barang = request.form['tgl_barang']
		jumlah_keterangan = request.form['jumlah_keterangan']
		keterangan = request.form['keterangan']
		data = (id_barang, tgl_barang, jumlah_keterangan, keterangan)
		model = Pembelian()
		model.insertDB(data)
		return redirect(url_for('pembelian.html'))
	else:
		return render_template('insertPembelian.html')

@aplication.route('/update/<id_pembelian>')
def update(id_pembelian):
	model = Pembelian()
	data = model.getDBbyId_pembelian(id_pembelian)
	return render_template('updatePembelian.html', data= data)

@aplication.route('/update_process', methods=['GET', 'POST'])
def update_process():
	id_barang = request.form['id_barang']
	tgl_barang = request.form['tgl_barang']
	jumlah_keterangan = request.form['jumlah_keterangan']
	keterangan = request.form['keterangan']
	data = (id_barang, tgl_barang, jumlah_keterangan, keterangan, id_pembelian)
	model = Pembelian()
	model.updateDB(data)
	return redirect(url_for('pembelian'))

@aplication.route('/delete/<no>')
def delete(id_pembelian):
	model = Pembelian()
	model.deleteDB(id_pembelian)
	return redirect(url_for('pembelian'))

if __name__ == '__main__':
	aplication.run(debug=True)
