import pymysql
import config

db = cursor = None

class Mcart:
	def __init__(self, email=None, nama_produk=None, jumlah=None, total=None, harga=None):
		self.email = email
		self.nama_produk = nama_produk
		self.jumlah = jumlah
		self.total = total
		self.harga = harga

	def openDB(self):
		global db, cursor
		db = pymysql.connect(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	def selectDB(self):
		self.openDB()
		cursor.execute("SELECT * FROM cart")
		container = []
		for no,email,nama_produk,harga,jumlah,total in cursor.fetchall():
			container.append((no,email,nama_produk,harga,jumlah,total))
		self.closeDB()
		return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO cart (email, nama_produk, jumlah, harga, total) VALUES ('%s','%s','%s','%s','%s')" % data)
		db.commit()
		self.closeDB()

	def getDBbyNo(self, no):
		self.openDB()
		cursor.execute(" SELECT * FROM cart WHERE no='%s'" % no)
		datac = cursor.fetchone()
		return datac

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE cart SET email='%s', nama_produk='%s', harga='%s', jumlah='%s ',  total='%s' WHERE no='%s'" % datac)
		db.commit()
		self.closeDB()

	def deleteDB(self, email):
		self.openDB()
		cursor.execute("DELETE FROM cart WHERE email='%s'" % email)
		db.commit()
		self.closeDB() 

class Musername:
	def __init__ (self, email=None, password=None, nama=None, tanggal_lahir=None, jenis_kelamin=None, no=None, no_telp=None, alamat=None):
		self.no = no
		self.email = email
		self.password = password
		self.nama = nama
		self.tanggal_lahir = tanggal_lahir
		self.jenis_kelamin = jenis_kelamin
		self.no_telp = no_telp
		self.alamat = alamat

	def openDB (self):
		global db, cursor
		db = pymysql.connect(
			config.DB_HOST,
			config.DB_USER,
			config.DB_PASSWORD,
			config.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	def selectDB(self):
		self.openDB()
		cursor.execute("SELECT * FROM user")
		container = []
		for no,email,password,nama,tanggal_lahir,jenis_kelamin,no_telp,alamat in cursor.fetchall():
			container.append((no,email,password,nama,tanggal_lahir,jenis_kelamin,no_telp,alamat))
		self.closeDB()
		return container

	def authenticate(self):
		self.openDB()
		cursor.execute("SELECT COUNT(*) FROM user WHERE email = '%s' AND password = '%s'" % (self.email, self.password))
		count_account = (cursor.fetchone())[0]
		self.closeDB()
		return True if count_account>0 else False

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO user (email, password, nama, tanggal_lahir, jenis_kelamin, no_telp, alamat) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % data)
		db.commit()
		self.closeDB()

	def getDBbyNo(self, no):
		self.openDB()
		cursor.execute("SELECT * FROM user WHERE no='%s'" % no)
		data = cursor.fetchone()
		return data

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE user SET email='%s', password='%s', nama='%s', tanggal_lahir='%s', jenis_kelamin='%s', no_telp='%s', alamat='%s' WHERE no='%s' " % data)
		db.commit()
		self.closeDB()

	def deleteDB(self, no):
		self.openDB()
		cursor.execute("DELETE FROM user WHERE no='%s'" % no)
		db.commit()
		self.closeDB()


class Mproduk:
	def __init__(self, nama_produk=None, gambar=None, diskripsi=None, harga=None):
		self.nama_produk = nama_produk
		self.gambar = gambar
		self.diskripsi = diskripsi
		self.harga =  harga

	def openDB(self):
		global db, cursor
		db = pymysql.connect(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	def selectDB(self):
		self.openDB()
		cursor.execute("SELECT * FROM produk")
		container = []
		for no,nama_produk,gambar,diskripsi,harga in cursor.fetchall():
			container.append((no,nama_produk,gambar,diskripsi,harga))
		self.closeDB()
		return container

	def insertDB(self, datap):
		self.openDB()
		cursor.execute("INSERT INTO produk (nama_produk, gambar, diskripsi, harga) VALUES ('%s','%s','%s','%s')" % datap)
		db.commit()
		self.closeDB()

	def getDBbyNo(self, no):
		self.openDB()
		cursor.execute(" SELECT * FROM produk WHERE no='%s'" % no)
		data = cursor.fetchone()
		return data

	def updateDB(self, datap):
		self.openDB()
		cursor.execute("UPDATE produk SET  nama_produk='%s', gambar='%s', diskripsi='%s ',  harga='%s' WHERE no=%s " % datap)
		db.commit()
		self.closeDB()

	def deleteDB(self, no):
		self.openDB()
		cursor.execute("DELETE FROM produk WHERE no='%s'" % no)
		db.commit()
		self.closeDB()