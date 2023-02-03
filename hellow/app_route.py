from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h2>halaman home</h2><a href="profile">menuju profile</a>';

@app.route('/profile')
def profile():
	return '<h2>halaman profile</h2><a href="/">menuju home</a>';

@app.route('/nama/<name>')
def nama(name):
	return '<h2>hallo  '+str(name)+'</h2>';

@app.route('/umur/<int:age>')
def umur(age):
	return '<h2>Umurku '+str(age)+'</h2>';

if __name__ == '__main__':
	app.run(debug = True)