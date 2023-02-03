from flask_wtf import Form
from wtforms import FileField, SubmitField

class UploadForm(Form):
	file = FileField('pilih file yang mau di upload')
	submit = SubmitField('Upload')