from flask import Flask, render_template, request
from werkzeug import secure_filename
from models import DetailUpload
from datetime import datetime
import time
import os

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/Tupload/static/uploads'

#satuan byte
application.config['MAX_CONTENT_PATH'] = 10000000
@application.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		f = request.files['file']
		filename = application.config['UPLOAD_FOLDER'] + '/' + secure_filename(f.filename)
		date_time=datetime.now()
		data = (secure_filename(f.filename), date_time)
		model = DetailUpload()
		model.insertDB(data)
		container = []
		container = model.selectDB()
		try:
			f.save(filename)
			return render_template('upload_sukses.html', container=container, filename=secure_filename(f.filename))
		except:
			return render_template('upload_gagal.html')
	return render_template('form.html')

if __name__ == '__main__':
		application.run(debug=True)

#Muhammad Ilham Z