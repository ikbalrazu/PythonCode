import sqlite3

# connect with sqlite
conn = sqlite3.connect("books.db")

# we use cursor object to work with the database
c=conn.cursor()

# create table
#c.execute('''CREATE TABLE books (Titles TEXT, Pages INTEGER)''')


# insert data into table
#c.execute("INSERT INTO books VALUES ('raju',20)")

#c.execute('UPDATE books SET pages=100 where Titles="iqbal"')

#c.execute("ALTER TABLE books ADD book_id TEXT")
c.execute("ALTER table books RENAME TO book_id")
#c.execute("DELETE FROM books WHERE Titles='raju'")

#c.execute("SELECT * FROM books")

#print(c.fetchall())
conn.commit()
conn.close()

