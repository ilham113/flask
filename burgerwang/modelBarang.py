import pymysql
import config

db = cursor = None

class Barang:
	def __init__ (self, id_barang=None, nama_barang=None, stock_barang=None, harga_beli=None, harga_jual=None, keterangan=None):
		self.id_barang = id_barang
		self.nama_barang = nama_barang
		self.stock_barang = stock_barang
		self.harga_beli = harga_beli
		self.harga_jual = harga_jual

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
		cursor.execute("SELECT * FROM barang")
		container = []
		for id_barang,nama_barang,stock_barang,harga_beli,harga_jual in cursor.fetchall():
				container.append((id_barang,nama_barang,stock_barang,harga_beli,harga_jual))
		self.closeDB()
		return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO barang (id_barang,nama_barang,stock_barang,harga_beli,harga_jual) VALUES('%s', '%s', '%s', '%s', '%s')" % data)
		db.commit()
		self.closeDB()

	def getDBbyid_barang(self, id_barang):
		self.openDB()
		cursor.execute("SELECT * FROM barang WHERE id_barang='%s'" % id_barang)
		data = cursor.fetchone()
		return data

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE barang SET nama_barang='%s', stock_barang='%s', harga_beli='%s', harga_jual='%s' WHERE id_barang='%s'" % data)
		db.commit()
		self.closeDB()

	def deleteDB(self, id_barang):
		self.openDB()
		cursor.execute("DELETE FROM barang WHERE id_barang='%s'" % id_barang)
		db.commit()
		self.closeDB()