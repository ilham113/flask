from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Length, Email, URL

class KomentarForm(FlaskForm):
	nama = StringField('Nama:', validators=[Required('nama harus Di Isi!!'),Length(max=25)])
	email = StringField('Email:', validators=[Required('Email harus Di Isi!!'),Email('Alamat Email tidak Di tulis dengan benar!.')])
	url = StringField('URL:', validators=[Required('URL harus Di Isi!!'), URL()])
	komentar = TextAreaField('komentar:', validators=[Required('komentar harus Di Isi !!')])
	submit = SubmitField('kirim')
	