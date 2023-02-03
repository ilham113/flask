from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField,  SubmitField

class PersonalFrom(FlaskForm):
	nama = StringField('Nama:')
	nim = StringField('NIM:')
	prodi = StringField('Prodi:')
	email = StringField('Email:')
	nomor = StringField('Nomor HP:')
	alamat = TextAreaField('Alamat:')
	jenisKelamin = RadioField('Jenis Kelamin:', choices=[('P', 'Pria'),('W','Wanita')])
	agama = SelectField('Agama:', choices=[('1','Islam'),('2','Protestan'),('3','Katolik'),('4','Hindu'),('5','Budha')])
	submit = SubmitField('kirim')
	
#Muhammad Ilham Z