import sqlite3

with open("library.db","w") as f:
    pass

con = sqlite3.connect("library.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE Books (Title TEXT, Author TEXT, Year_Published INTEGER, Genre TEXT)")

data = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]
cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", data)

cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = \"1984\"")

cursor.execute("SELECT Title, Author FROM Books WHERE Genre = \"Dystopian\"")
for title, author in cursor.fetchall():
    print(f"{title} {author}")

cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
data = [
    ("To Kill a Mockingbird", 4.8),
    ("1984", 4.7),
    ("The Great Gatsby", 4.5)
]
for title, rating in data:
    cursor.execute("UPDATE Books SET Rating = ? WHERE title = ?", (rating, title))

cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
for title, author, year_published, genre, rating in cursor.fetchall():
    print(title,author, year_published,genre, rating)

con.commit()
con.close()