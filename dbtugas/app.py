from flask import Flask, render_template, request, redirect, url_for
from models import MBukuTelepon 

application = Flask(__name__)

@application.route('/')
def index():
	model = MBukuTelepon()
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
		model = MBukuTelepon()
		model.insertDB(data)
		return redirect(url_for('index'))
	else:
		return render_template('insert_form.html')

if __name__ == '__main__':
	application.run(debug=True)

#Muhammad Ilham 