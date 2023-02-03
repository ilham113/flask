from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
	return '<h2>hellow flask</h2><p>M.ilham'

if __name__ == '__main__':
	application.run(debug=True)