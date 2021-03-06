import sqlite3

def createTable():
    conn = sqlite3.connect("settings.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS settings
    (playerName TEXT PRIMARY KEY NOT NULL,
    sensitivity INTEGER);''')
    conn.commit()
    conn.close()

def setSensitivity(name, sen):
	conn = sqlite3.connect("settings.db")
	if (checkTableExists(conn, settings) == False):
		createTable()
	inputval = (name, sen)
	c = conn.cursor()
	c.execute('''INSERT INTO settings(sensitivity) where playerName = (?) VALUES(?)''', (inputval,))
	conn.commit()
	conn.close()

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
		
setSesitivity(player, num)