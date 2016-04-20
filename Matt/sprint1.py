import sqlite3

def createTable():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scores
    (playerID INTEGER PRIMARY KEY NOT NULL,
    playerName TEXT NOT NULL,
    playerScore INTEGER NOT NULL);''')
    conn.commit()
    conn.close()

def addScore(name, score):
    inputvals = (name, score)
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("INSERT INTO scores (playerName, playerScore) VALUES(?, ?)", inputvals)
    conn.commit()
    conn.close()

def getScore(name):
    t = name
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute('''SELECT playerName, playerScore FROM scores WHERE playerName = ?''', (t,))
    print (c.fetchone())
    conn.close()

def allScores():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute("SELECT * FROM scores")
    print(c.fetchall())
    conn.close()

def removeScore(name):
    t = name
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute('''DELETE playerID, playerName, playerScore, FROM scores WHERE playerName = ?''', (t,))
    conn.commit()
    conn.close()

createTable()
addScore("Matt", 100)
addScore("Stacie", 50)
getScore("Matt")
allScores()