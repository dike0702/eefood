import sqlite3

dbname  = 'eefood.db'
conn    = sqlite3.connect(dbname)

conn.close()