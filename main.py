import json
from library import librarian

FILE = "books.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

library_data = load_data()

while True:
    print("\n1- Add book")
    print("2- Show books")
    print("3- Delete book")
    print("4- Borrow book")
    print("5- Return book")
    print("6- Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        librarian.add_book(library_data, title, author, isbn)
        save_data(library_data)

    elif choice == "2":
        librarian.display_books(library_data)

    elif choice == "3":
        isbn = input("ISBN: ")
        librarian.remove_book(library_data, isbn)
        save_data(library_data)

    elif choice == "4":
        isbn = input("ISBN: ")
        librarian.check_out_book(library_data, isbn)
        save_data(library_data)

    elif choice == "5":
        isbn = input("ISBN: ")
        librarian.return_book(library_data, isbn)
        save_data(library_data)

    elif choice == "6":
        print("Goodbye")
        break
    