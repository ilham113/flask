import pymysql
import config

db = cursor = None

class Popupstore():
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password

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

    def authenticate(self):
        self.openDB()
        cursor.execute("SELECT COUNT(*) FROM user WHERE username = '%s' And password = '%s'" % (self.username, self.password))
        count_account = (cursor.fetchone())[0]
        self.closeDB()
        return True if count_account > 0 else False

    def accountType(self):
        self.openDB()
        cursor.execute("SELECT * FROM user WHERE username = '%s' AND password = '%s'" % (self.username, self.password))
        account = (cursor.fetchone())
        self.closeDB()
        return 'admin' if account[1] == 'admin' else 'user'




        # self.openDB()
        # cursor.execute("SELECT * COUNT(*) FROM user WHERE username = '%s' And password = '%s' % (self.username, self.password) ")
        # count_account = (cursor.fetchone())[0]
        # self.closeDB()
        # if count_account > 0 and account[1] == 'admin':
        #     return 0
        # elif count_account > 0:
        #     return 1