from flask import Flask, render_template, request
from models import PersonalFrom

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#123456&*()'

#Muhammad Ilham Z
@application.route('/', methods =['GET', 'POST'])
def index():
	form = PersonalFrom()
	if request.method == 'POST':
		if form.validate():
			nama = form.nama.data
			nim = form.nim.data
			prodi = form.prodi.data
			email = form.email.data
			nomor = form.nomor.data
			alamat = form.alamat.data
			jenisKelamin = form.jenisKelamin.data
			agama = int(form.agama.data)
			return render_template('response.html', nama=nama, alamat=alamat, jenisKelamin=jenisKelamin, agama=agama, nim=nim, prodi=prodi, email=email, nomor=nomor)
		else:
			errors = form.errors.items()
			return render_template('form.html', form=form, errors=errors)

	return render_template('form.html', form=form)

if __name__ == '__main__':
	application.run(debug=True)