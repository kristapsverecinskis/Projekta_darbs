import sqlite3

con = sqlite3.connect("paroles.db")
c = con.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Majaslapa TEXT,
        Lietotajvards TEXT,
        Shifreta_parole TEXT
    )
''')

con.commit()
con.close()
