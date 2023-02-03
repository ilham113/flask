from flask import Flask, render_template
from models import MBukuTelepon 

application = Flask(__name__)

@application.route('/')
def index():
	model = MBukuTelepon()
	container = []
	container = model.selectDB()
	return render_template('index.html', container=container)

if __name__ == '__main__':
	application.run(debug=True)

#Muhammad Ilham 