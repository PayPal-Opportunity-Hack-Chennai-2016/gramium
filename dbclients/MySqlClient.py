import MySQLdb

class MySqlClient:

    mysql_host = "192.168.120.232"
    mysql_user = "gramium"
    mysql_pass = "Demo@1234"
    mysql_database = "gramium"
    mysql_connection = None

    def __init__(self):
        return

    def getConnection(self):
        try:
            self.mysql_connection = MySQLdb.connect(self.mysql_host, self.mysql_user, self.mysql_pass)
            print "Mysql Connection Established Successfully"
            return self.mysql_connection
        except:
            print "Mysql Connection Established Failed"
            return None

    def testConnection(self):
        try:
            mysql_connection =  MySQLdb.connect(self.mysql_host, self.mysql_user, self.mysql_pass)
            mysql_connection.close()
            print "Mysql Connection Test Successful" + "{Host:" + self.mysql_host + "},{User:" + self.mysql_user + "}"
            return 0
        except:
            print "Mysql Connection Test Failed" + "{Host:" + self.mysql_host + "},{User:" + self.mysql_user + "}"
            return 1

    def getDatabaseConnection(self, database=None):
        if database == None:
            database = self.mysql_database
        if self.testConnection() == 0:
            try:
                self.mysql_connection =  MySQLdb.connect(self.mysql_host, self.mysql_user, self.mysql_pass, database)
                print "Database Connection Successful" + "{Database:" + database + "}"
                return self.mysql_connection
            except:
                print "Database Error. Check if database exists" + "{Database:" + database + "}"
                return None

    def closeConnection(self):
        status_code = 0
        try:
            self.mysql_connection.close()
            print "Mysql Connection closed Successfully"
        except:
            status_code = 1
            print "Mysql Connection could not be closed"
        return status_code

if __name__ == "__main__":
    client = MySqlClient()
    db = client.getDatabaseConnection()
    client.closeConnection()
