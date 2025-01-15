import sqlite3

filename = "roster.db"

with open(filename,"w") as f:
    pass

con = sqlite3.connect(filename)
cursor = con.cursor()

cursor.execute("CREATE TABLE Roster (Name TEXT, Species TEXT, Age Integer)")

data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", data)

cursor.execute("UPDATE Roster SET Name = \"Ezri Dax\" WHERE Name = \"Jadzia Dax\"")

cursor.execute("SELECT Name, Age FROM Roster Where Species = \"Bajoran\"")
characters = cursor.fetchall()
for name, age in characters:
    print(f"{name} {age}")

cursor.execute("DELETE FROM Roster Where Age > 100")

cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

data = [
    ("Benjamin Sisko", "Captain"),
    ("Ezri Dax", "Lieutenant"),
    ("Kira Nerys", "Major")
]
for name, rank in data:
    cursor.execute("UPDATE Roster SET Rank = ? Where Name = ?", (rank, name))

cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
for name, species, age, rank in cursor.fetchall():
    print(f"{name} is {species} and {age} years old. It's rank is {rank}")

con.commit()
con.close()