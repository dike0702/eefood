import sqlite3

dbname = "eefood.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# cur.execute(
#     'CREATE TABLE Restaurants(name VARCHAR(80) PRIMARY KEY,addr VARCHAR(50),phone VARCHAR(16),table REAL,genre char(15))')

cur.execute("""
    CREATE TABLE IF NOT EXISTS Restaurants(
        name VARCHAR(80) PRIMARY KEY,
        addr VARCHAR(50),
        phone VARCHAR(16),
        seats REAL,
        genre char(15),
        img BLOB
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        name VARCHAR(40) PRIMARY KEY,
        id INTEGER UNIQUE
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS menu(
        RestaurantName VARCHAR(80) PRIMARY KEY,
        ingredient STRING,
        price DECIMAL(10,2),
        quantity REAL,
        FOREIGN KEY(RestaurantName) REFERENCES Restaurants(name)
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS Reservation(
        RestaurantName VARCHAR(80) PRIMARY KEY,
        UserName VARCHAR(40),
        seats REAL,
        openTime DECIMAL(2,2),
        closeTime DECIMAL(2,2),
        FOREIGN KEY(RestaurantName) REFERENCES Restaurants(name),
        FOREIGN KEY(UserName) REFERENCES Users(name),
        FOREIGN KEY(seats) REFERENCES Restaurants(seats)
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS Review(
        RestaurantName VARCHAR(80) PRIMARY KEY,
        UserName VARCHAR(40),
        rate REAL CHECK(rate >= 0 AND rate <= 5)
    );
""")

# cur.execute(create_table_sql)

conn.commit()

cur.close()
conn.close()