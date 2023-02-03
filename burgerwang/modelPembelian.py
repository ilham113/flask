import pymysql
import config

db = cursor = None

class Pembelian:
	def __init__ (self, id_pembelian=None, id_barang=None, tgl_pembelian=None, jumlah_pembelian=None, keterangan=None):
		self.id_pembelian = id_pembelian
		self.id_barang = id_barang
		self.tgl_pembelian = tgl_pembelian
		self.jumlah_pembelian = jumlah_pembelian
		self.keterangan = keterangan

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
		cursor.execute("SELECT * FROM pembelian")
		container = []
		for id_pembelian, id_barang, tgl_pembelian, jumlah_pembelian, keterangan in cursor.fetchall():
				container.append(( id_pembelian, id_barang, tgl_pembelian, jumlah_pembelian, keterangan))
		self.closeDB()
		return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO pembelian (id_barang, tgl_pembelian, jumlah_pembelian, keterangan) VALUES('%s','%s','%s','%s')" % data)
		db.commit()
		self.closeDB()

	def getDBId_pembelian(self, id_pembelian):
		self.openDB()
		cursor.execute("SELECT * FROM pembelian WHERE id_pembelian='%s' " % id_pembelian)
		data = cursor.fetchone()
		return data

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE pembelian SET id_barang='%s', tgl_pembelian='%s', jumlah_pembelian='%s', keterangan='%s' WHERE id_pembelian=%s" % data)
		db.commit()
		self.closeDB()

	def deleteDB(self, id_pembelian):
		self.openDB()
		cursor.execute("DELETE FROM pembelian WHERE id_pembelian=%s" % id_pembelian)
		db.commit()
		self.closeDB()



