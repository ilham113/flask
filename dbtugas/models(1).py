import pymysql
import config

db = cursor = None

class Mdaftarmhs:
	def __init__(self, no=None,nama=None,nim=None,prodi=None,fakultas=None):
		self.no = no
		self.nama = nama
		self.nim = nim
		self.prodi = prodi
		self.fakultas = fakultas

	def openDB(self):
		global db, cursor
		db = pymysql.connect(config.DB_HOST, config.DB_USER, config.DB_PASSWORD, config.DB_NAME)
		cursor = db.cursor()
	
	def closeDB(self):
		global db, cursor
		db.close()

	def selectDB(self):
		self.openDB()
		cursor.execute("SELECT * FROM daftarmhs")
		container = []
		for no,nama,nim,prodi,fakultas in cursor.fetchall():
			container.append((no,nama,nim,prodi,fakultas))
		self.closeDB()
		return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO daftarmhs (nama, nim, prodi, fakultas) VALUES ('%s','%s','%s','%s')" % data)
		db.commit()
		self.closeDB()

	def getDBbyNo(self, no):
		self.openDB()
		cursor.execute(" SELECT * FROM daftarmhs WHERE no='%s'" % no)
		data = cursor.fetchone()
		return data

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE daftarmhs SET nama='%s', nim='%s', prodi='%s', fakultas='%s' WHERE no=%s " % data)
		db.commit()
		self.closeDB()

	def deleteDB(self, no):
		self.openDB()
		cursor.execute("DELETE FROM daftarmhs WHERE no='%s'" % no)
		db.commit()
		self.closeDB()


#Muhammad Ilham 