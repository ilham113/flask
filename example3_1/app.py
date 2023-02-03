from flask import Flask, render_template
from models import Lingkaran

application = Flask(__name__)

@application.route('/')
def index():
	str_var = 'pengembangan aplikasi web Flask'
	int_var = 15
	float_var = 29.05
	list_var = [1,2,3]
	dict_var = {'satu': 1,'dua':2,'tiga':3}
	model = Lingkaran(30.0)

	return render_template('hello.html',str_var=str_var,int_var=int_var,float_var=float_var,list_var=list_var,dict_var=dict_var,model=model)

if __name__ == '__main__':
	application.run(debug=True)