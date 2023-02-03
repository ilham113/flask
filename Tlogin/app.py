from flask import Flask, render_template, session, request, redirect, url_for
from models import Mpengguna

application  = Flask(__name__)
application.config['SECRET_KEY'] = '1234567890'

@application.route('/')
def index():
	if 'username' in session :
		username = session['username']
		return render_template('index.html', username=username)
	return redirect(url_for('login'))
@application.route('/admin')
def admin():
	if 'username' in session :
		username = session['username']
		return render_template('admin.html', username=username)
	return redirect(url_for('login'))

@application.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST' :
		username = request.form['username']
		password = request.form['password']
		#level = ['level']
		pengguna = Mpengguna(username, password)
		if pengguna.authenticate() :
			session['username'] = username
			if session['username'] == 'admin':
				return redirect(url_for('admin'))
			else :
				return redirect(url_for('index'))	
		msg = 'username/password salah'
		return render_template('form.html', msg=msg)
	return render_template('form.html')

@application.route('/logout')
def logout():
	session.pop('username', '')
	return redirect(url_for('index'))

if __name__ == '__main__':
	application.run(debug=True)

#muhammad Ilham