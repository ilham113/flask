from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField,  SubmitField
from wtforms.validators import Required, Length, Email

class PersonalFrom(FlaskForm):
	nama = StringField('Nama:', validators=[Required('nama harus Di Isi!!'),Length(max=25)])
	nim = StringField('NIM:')
	prodi = StringField('Prodi:')
	email = StringField('Email:', validators=[Required('Email harus Di Isi!!'),Email('Alamat Email tidak Di tulis dengan benar!.')])
	nomor = StringField('Nomor HP:')
	alamat = TextAreaField('Alamat:')
	jenisKelamin = RadioField('Jenis Kelamin:', choices=[('P', 'Pria'),('W','Wanita')])
	agama = SelectField('Agama:', choices=[('1','Islam'),('2','Protestan'),('3','Katolik'),('4','Hindu'),('5','Budha')])
	submit = SubmitField('kirim')
	
#Muhammad Ilham Z