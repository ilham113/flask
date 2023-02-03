import pymysql
import config

db=cursor=None

class DetailUpload:
	def __init__(self, id_file=None, nama_file=None, tgl_upload=None):
		self.id_file=id_file
		self.nama_file=nama_file
		self.tgl_file=tgl_upload

	def openDB(self):
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
		cursor.execute("SELECT * FROM uploadfile")
		container = []
		for id_file,nama_file,tgl_upload in cursor.fetchall():
			container.append((id_file,nama_file,tgl_upload))
		self.closeDB()
		return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO uploadfile (nama_file, tgl_upload) VALUES('%s', '%s')" %data)
		db.commit()
		self.closeDB()

#Muhammad Ilham Z