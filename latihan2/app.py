from flask import Flask, render_template
from models import Model2

application = Flask(__name__)

nom1='1'
nama1='Muhammad Umar'
nim1='182100210'
prodi1='Teknik Informatika'
nom2='2'
nama2='Jamaludin'
nim2='182100205'
prodi2='Teknik Informatika'
namaku='Muhammad Ilham Z'

@application.route('/')
def index():
	model=Model2()

	model.setTitle('DAFTAR MAHASISWA')
	model.setDate('2020/2021')
	model.setNom1(nom1)
	model.setNama1(nama1)
	model.setNim1(nim1)
	model.setProdi1(prodi1)
	model.setNom2(nom2)
	model.setNama2(nama2)
	model.setNim2(nim2)
	model.setProdi2(prodi2)
	model.setNamaku(namaku)

	return render_template('hello.html',judul=model.getTitle(),tahun=model.getDate(),nom1=model.getNom1(),nama1=model.getNama1(),nim1=model.getNim1(),prodi1=model.getProdi1(),nom2=model.getNom2(),nama2=model.getNama2(),nim2=model.getNim2(),prodi2=model.getProdi2(),namaku=model.getNamaku())

if __name__ == '__main__':
	application.run(debug=True)