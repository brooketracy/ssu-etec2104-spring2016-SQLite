import sqlite3

def createTable():
    conn = sqlite3.connect("settings.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS settings
    (playerName TEXT PRIMARY KEY NOT NULL,
    sensitivity INTEGER);''')
    conn.commit()
    conn.close()

def getSensitivity(name):
	inputval = name
	conn = sqlite3.connect("settings.db")
	if (checkTableExists(conn, settings) == False):
		createTable()
	c = conn.cursor()
	c.execute('''SELECT sensitivity FROM settings where playerName = ?''', (inputval,))
	conn.close()
	return(c.fetchone())

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True
		
getSensitivity(name)