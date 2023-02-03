from flask import Flask
from models import Model1

application = Flask(__name__)

@application.route('/')
def index():
	model = Model1()
	return model.getText()

if __name__ == '__main__':
	application.run(debug=True)