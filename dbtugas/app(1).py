from flask import Flask, render_template, request, redirect, url_for
from models import Mdaftarmhs 

application = Flask(__name__)

@application.route('/')
def index():
	model = Mdaftarmhs()
	container = []
	container = model.selectDB()
	return render_template('index.html', container=container)

@application.route('/insert', methods=['GET','POST'])
def insert():
	if request.method == 'POST':
		nama = request.form['nama']
		nim = request.form['nim']
		prodi = request.form['prodi']
		fakultas = request.form['fakultas']
		data = (nama, nim, prodi, fakultas)
		model = Mdaftarmhs()
		model.insertDB(data)
		return redirect(url_for('index'))
	else:
		return render_template('insert_form.html')

@application.route('/update/<no>')
def update(no):
	model = Mdaftarmhs()
	data = model.getDBbyNo(no)
	return render_template('update_form.html', data=data,)

@application.route('/update_process', methods=['GET','POST'])
def update_process():
	no = request.form['no']
	nama = request.form['nama']
	nim = request.form['nim']
	prodi = request.form['prodi']
	fakultas = request.form['fakultas']
	data = (nama, nim, prodi, fakultas, no)
	model =Mdaftarmhs()
	model.updateDB(data)
	return redirect(url_for('index'))

@application.route('/delete/<no>')
def delete(no):
	model = Mdaftarmhs()
	model.deleteDB(no)
	return redirect(url_for('index'))

if __name__ == '__main__':
	application.run(debug=True)

#Muhammad Ilham 