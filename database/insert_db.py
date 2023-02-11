import sqlite3

dbname = "eefood.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('INSERT INTO Restaurants VALUES("CHIN CHIN EXPRESS", "2304 E Johnson Ave, Jonesboro, AR 72401", "870-203-6188", 10, "Chinese")')
# # cur.execute()
# # cur.execute()

conn.commit()
cur.close()
conn.close()