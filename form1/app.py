from flask import Flask, render_template, request
from model import PersonalFrom

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#123456&*()'

#Muhammad Ilham Z
@application.route('/', methods =['GET', 'POST'])
def index():
	form = PersonalFrom()
	if request.method == 'POST':
		nama = form.nama.data
		alamat = form.alamat.data
		jenisKelamin = form.jenisKelamin.data
		agama = int(form.agama.data)
		hobi1 = form.hobi1.data
		hobi2 = form.hobi2.data
		hobi3 = form.hobi3.data
		return render_template('renponse.html', nama=nama, alamat=alamat, jenisKelamin=jenisKelamin, agama=agama, hobi1=hobi1, hobi2=hobi2, hobi3=hobi3)

	return render_template('form.html', form=form)

if __name__ == '__main__':
	application.run(debug=True)