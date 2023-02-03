class Model5:
	def __init__ (self, title=None, date=None, content=None, nama=None):
		self.title = title
		self.date = date
		self.content = content
		self.nama = nama

	def setTitle(self, title):
		self.title = title

	def getTitle(self):
		return self.title

	def setDate(self, date):
		self.date = date

	def getDate(self):
		return self.date

	def setContent(self, content):
		self.content = content

	def getContent(self):
		return self.content

	def setNama(self, nama):
		self.nama = nama

	def getNama(self):
		return self.nama