from flask import Flask, render_template
from models import Model24

application = Flask(__name__)

@application.route('/')
def index():
	model = Model24()
	return render_template('hello.html', model=model)

if __name__ == '__main__':
	application.run(debug=True)