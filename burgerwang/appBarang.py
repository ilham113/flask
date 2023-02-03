from flask import Flask, render_template, request, redirect, url_for
from modelBarang import barang 

application = Flask(__name__)

@application.route('/')
def index():
	model = paw_flask()
	container = []
	container = model.selectDB()
	return render_template('barang.html', container=container)

@application.route('/insert', methods=['GET', 'POST'])
def insert():
	if request.method == 'POST':
		id_barang = request.form['id_barang']
		nama_barang = request.form['nama_barang']
		stock_barang = request.form['stock_barang']
		harga_beli = request.form['harga_beli']
		harga_jual = request.form['harga_jual']
		data = (nama_barang, stock_barang, harga_beli, harga_jual, id_barang)
		model = barang()
		model.insertDB(data)
		return redirect(url_for('barang'))
	else:
		return render_template('insert_form.html')

@application.route('/update/<id_barang>')
def update(id_barang):
	model = barang()
	data = model.getDBbyid_barang(id_barang)
	return render_template('update_from.html', data=data)

@application.route('/update_process', methods=['GET', 'POST'])
def update_process():
	id_barang = request.form['id_barang']
	nama_barang = request.form['nama_barang']
	stock_barang = request.form['stock_barang']
	harga_beli = request.form['harga_beli']
	harga_jual = request.form['harga_jual']
	ketarangan = request.form['ketarangan']
	data = (nama_barang, stock_barang, harga_beli, harga_jual, ketarangan)
	model = barang()
	model.updateDB(data)
	return redirect(url_for('barang'))

@application.route('/delete/<id_barang>')
def delete(id_barang):
	model = barang()
	model.deleteDB(id_barang)
	return redirect(url_for('barang'))

if __name__ == '__main__':
	application.run(debug=True)