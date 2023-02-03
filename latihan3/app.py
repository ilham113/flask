from flask import Flask, render_template
from models import Lingkaran

application = Flask(__name__)

@application.route('/')
def index():
	a = 20
	b = 30
	c = 20
	str_var = 'pengembangan aplikasi web Flask'
	int_var = 75
	float_var = 123.05
	list_var = [1,2,3]
	dict_var = {'satu': 1,'dua':2,'tiga':3}
	model = Lingkaran(42.0)
	navigasi = [
	('/', 'home'),
	('/profile', 'profile'),
	('/product', 'product'),
	('/contact', 'contact'),
	]

	return render_template('index.html',navigasi=navigasi,a=a,b=b,c=c,str_var=str_var,int_var=int_var,float_var=float_var,list_var=list_var,dict_var=dict_var,model=model)

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