from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SelectField, BooleanField, SubmitField

class PersonalFrom(FlaskForm):
	nama = StringField('Nama:')
	alamat = TextAreaField('Alamat:')
	jenisKelamin = RadioField('Jenis Kelamin:', choices=[('P', 'Pria'),('W','Wanita')])
	agama = SelectField('Agama:', choices=[('1','Islam'),('2','Protestan'),('3','Katolik'),('4','Hindu'),('5','Budha')])
	hobi1 = BooleanField('Nyanyi')
	hobi2 = BooleanField('Olahraga')
	hobi3 = BooleanField('Mancing')
	submit = SubmitField('kirim')
	