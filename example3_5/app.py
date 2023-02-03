from flask import Flask,render_template

application  = Flask(__name__)

@application.route('/')
def index():
	navigasi = [
	('/', 'home'),
	('/profile', 'profile'),
	('/product', 'product'),
	('/contact', 'contact'),
	]
	return render_template('index.html',navigasi=navigasi)

@application.route('/profile')
def profile():
	return '<h2>profile</h2>'

@application.route('/product')
def product():
	return '<h2>product</h2>'

@application.route('/contact')
def contact():
	return '<h2>contact</h2>'

if __name__ == '__main__':
	application.run(debug=True)