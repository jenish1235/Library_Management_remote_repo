import mysql.connector
#connection to mysql
db = mysql.connector.connect(host="localhost",
                             password= "root",
                             user="root",
                             database="library")
cursor = db.cursor()

#inserting a book

def add_book(books, subject):
    cursor.execute("INSERT INTO books('Oswal', 'maths') VALUES (%s, %s, %s)")
    db.commit()

def display_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for books in books:
        print(book)

#issueing book

def issue_book(book_name):
    cursor.execute("UPDATE books SET available = FALSE WHERE name = %s", (book_name,))
    db.commit()
    
#submitting a book

def submit_book(book_name):
    cursor.execute("UPDATE books SET available = TRUE WHERE name = %s",(book_name))
    db.commit()

#example usage
add_book("The Great Lion", "english")
add_book("Swoonman", "english")

display_books()

issue_book(1)
display_books()

submit_book(1)
display_books()

#close the connection

db.close()


