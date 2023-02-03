from flask import Flask, render_template
from models import Model5

application = Flask(__name__)

content = 'ini adalah berita terbaru akan tetapi berasal dari orang lama'
nama = 'Muhammad Ilham.Z'

@application.route('/')
def index():
	model = Model5()

	model.setTitle('Berita Terkini')
	model.setDate('18/08/2019')
	model.setContent(content)
	model.setNama(nama)

	return render_template('hello.html',judul=model.getTitle(),tanggal=model.getDate(),isi=model.getContent(),nama=model.getNama())

if __name__ == '__main__':
	application.run(debug=True)