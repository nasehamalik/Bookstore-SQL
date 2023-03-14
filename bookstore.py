import sqlite3
db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()

# Create a table called books in the database
cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
'''
)
# Create variables storing the id, title and author and quantity for each book
id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

id2 = 3002
title2 = 'Harry Potter and the Philosophers Stone'
author2 = 'J.K. Rowling'
qty2 = 40

id3 = 3003
title3 = 'The Lion, the Witch and the Wardrobe'
author3 = 'C. S. Lewis'
qty3 = 25

id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkien'
qty4 = 37

id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Carroll'
qty5 = 12

# Create a list containing the id, title, author and quantity of each book
bookinfo = [(id1,title1,author1,qty1),(id2,title2,author2,qty2),(id3,title3,author3,qty3),(id4,title4,author4,qty4),(id5,title5,author5,qty5)]

# Insert the book information in the list into the table
cursor.executemany(''' INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''',
bookinfo)
db.commit()

while True:
    # Create a menu for the bookstore clerk
    # Request the clerk to choose an option from the menu
    menu = input("""Select one of the following options below:
    1 - Enter a new book
    2 - Update exisiting book information
    3 - Delete a book 
    4 - Seach for a specific book
    0 - Exit
    : """).lower()

    # Create a programme to enable to the clerk to add new books to the database
    if menu == '1':
        pass
        id = input("Enter the id of the book: ").lower()
        title = input("Enter the title of the book: ").lower()
        author = input("Enter the author of the book: ").lower()
        qty = input("Enter the quantity of the book: ").lower()
        cursor.execute (''' INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''',
        (id, title, author, qty))
        print("Your new book has been added to the database")
        db.commit()

    # Create a programme to enable to the clerk to update book information
    if menu == '2':
        pass
        if bookid:
            bookid = bookid[0][0]
            updatebook = input("Which field would you like to update, the id, title, author or quantity? ").lower()
            updatefield = input("Please enter the updated information: ").lower()
            cursor.execute('''UPDATE books SET id =? ''')
            if updatebook == "title":
                cursor.execute('''UPDATE books SET title = ? WHERE id = ?''', (updatefield, bookid))
            elif updatebook == "author":
                cursor.execute('''UPDATE books SET author = ? WHERE id = ?''', (updatefield, bookid))
            elif updatebook == "quantity":
                cursor.execute('''UPDATE books SET qty = ? WHERE id = ?''', (updatefield, bookid))
            elif updatebook == "id":
                cursor.execute('''UPDATE books SET id = ? WHERE id = ?''', (updatefield, bookid))
            print("The selected book has been updated ")
            db.commit()

    # Create a programme to enable to the clerk to delete books from the database
    if menu == '3':
        pass
        deletebook_title = input("Please enter the title of the book you would like to delete: ").lower()
        cursor.execute('''DELETE FROM books WHERE title = ? ''', (deletebook_title,))
        cursor.execute('''DROP TABLE books''')
        print("The selected book has been deleted")
        db.commit

    # Create a programme to enable to the clerk to search the database to find a specific book
    if menu == '4':
        pass
        id = input("Enter the id of the book you would like to search for").lower()
        cursor.execute('''SELECT title, author, qty FROM books WHERE id=? ''', (id,))
        book = cursor.fetchall()
        print(book)
        db.commit
    
    if menu == '0':
            print("Thank you for using this database, goodbye!")
            exit()
    else:
        print("You have unfortunately made the incorrect choice, please try again")
    db.close()
