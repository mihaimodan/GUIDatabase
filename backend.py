import sqlite3

# The function to create the database on startup.
def create():
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute(
        "CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"
    )
    conn.commit()
    conn.close()


# Function for the 'Add Entry' button.
def insert(title, author, year, isbn):
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute(
        "INSERT INTO bookstore VALUES (NULL, ?,?,?,?)", (title, author, year, isbn)
    )
    conn.commit()
    conn.close()


# Function for the 'View All' button.
def view():
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM bookstore")
    rows = curs.fetchall()  # We grab the selection and return it
    conn.close()
    return rows


# Function for the 'Search Entry' button.
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute(
        "SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?",
        (title, author, year, isbn),
    )
    rows = curs.fetchall()
    conn.close()
    return rows


# Function for the 'Delete' button.
def delete(id):
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute("DELETE FROM bookstore WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# Function for the 'Update' button.
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("database.db")
    curs = conn.cursor()
    curs.execute(
        "UPDATE bookstore SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",
        (title, author, year, isbn, id),
    )
    conn.commit()
    conn.close()


# TODO Function for the 'Close' button.
# def close(self):
#     return self.quit()


create()
