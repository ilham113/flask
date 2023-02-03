import pymysql
import config

db = cursor = None

class Penjualan:
	def __init__ (self, id_penjualan=None, id_barang=None, id_member=None, jumlah_penjualan=None, tgl_penjualan=None, keterangan=None):
		self.id_penjualan = id_penjualan
		self.id_barang = id_barang
		self.id_member = id_member
		self.jumlah_penjualan = jumlah_penjualan
		self.tgl_penjualan = tgl_penjualan
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
		cursor.execute("SELECT * FROM penjualan")
		container = []
		for id_penjualan, id_barang, id_member, jumlah_penjualan, tgl_penjualan, keterangan in cursor.fetchall():
				container.append((id_penjualan, id_barang, id_member, jumlah_penjualan,tgl_penjualan, keterangan))
		self.closeDB()
		return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO penjualan(id_penjualan, id_barang, id_member, jumlah_penjualan, tgl_penjualan, keterangan) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % data)
		db.commit()
		self.closeDB()

	def getDBbyId_penjualan(self, id_penjualan):
		self.openDB()
		cursor.execute("SELECT * FROM penjualan WHERE id_penjualan='%s'" % id_penjualan)
		data = cursor.fetchone()
		return data

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE penjualan SET id_barang='%s', id_member='%s', jumlah_penjualan='%s', tgl_penjualan='%s', keterangan='%s' WHERE id_penjualan=%s" % data)
		db.commit()
		self.closeDB()

	def deleteDB(self, id_penjualan):
		self.openDB()
		cursor.execute("DELETE FROM penjualan WHERE id_penjualan=%s" % id_penjualan)
		db.commit()
		self.closeDB()