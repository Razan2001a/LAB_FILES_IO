def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }

def remove_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return

    del library[isbn]

def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return

    if not library[isbn]["available"]:
        print("Book already borrowed.")
        return

    library[isbn]["available"] = False

def return_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
        return

    library[isbn]["available"] = True

def display_books(library):
    if not library:
        print("No books available.")
        return

    for isbn, book in library.items():
        status = "Available" if book["available"] else "Borrowed"
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")