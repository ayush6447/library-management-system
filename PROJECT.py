import pickle

import csv

# Book
# Dictionary to store book information
books = {
    1: {"book_id": 1, "title": "Book Title 1", "author": "Author 1", "genre": "Fiction", "copies": 3},
    2: {"book_id": 2, "title": "Book Title 2", "author": "Author 2", "genre": "Non-Fiction", "copies": 2},
    # Add more books as needed
}

# Dictionary to store checked-out book information
checked_out_books = {
    1: {"book_id": 1, "patron_name": "Author", "due_date": "yyyy-mm-dd"},
    # Add more checked-out books as needed
}

# Function to display the menu

def display_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")

    print("3. Search Book")

    print("4. Update Book")

    print("5. Delete Book")

    print("6. Save Books to Binary File")
    print("7. Load Books from Binary File")
    print("8. Save Books to CSV File")
    print("9. Load Books from CSV File")
    print("10. View Statistics")

    print("11. Clear All Data")

    print("12. Check Out Book")

    print("13. Return Book")

    print("14. View Checked-Out Books")

    print("15. Save Checked-Out Books to File")
    print("16. Load Checked-Out Books from File")

    print("17. Add Patron")

    print("18. View Patrons")
    print("19. Save Patrons to File")
    print("20. Load Patrons from File")
    print("21. Exit")

# Function to add a book.

def add_book(books):

    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author= input("Enter Author: ")
    genre = input("Enter Genre: ")
    copies+int(input("Enter Number of Copies: "))
    book =Book(book_id, title, author, genre, copies)
    books.append(book)
    print("Book added successfully!")

# Function to view all books

def view_books(books):

    print("\nBook List:")
    for book in books:
        print("""ID: {book.book_id}, Title: {book.title},
        Author: {book.author), Genre: {book.genre},
        Copies: {book.copies)""")

# Function to search for a book

def search_book(books):

    search_id = input("Enter Book ID to search: ")
    for book in books:
        if book.book_id == search_id:
            print("Book Found:")
            print("""ID: {book.book_id}, Title: {book.title},
            Author: {book.author}, Genre: {book.genre},
            Copies: {book.copies}""")
            return
    print("Book not found.")

# Function to update a book's information

def update_book(books):

    update_id = input("Enter Book ID to update: ")
    for book in books:
        if book.book_id == update_id:
            print("Current Book Information:")
            print("""ID: {book.book_id}, Title: {book.title},Author: {book.author}, Genre: {book.genre},Copies: {book.copies)""")
            book.title = input("Enter new Title: ")
            book.author = input("Enter new Author: ")
            book.genre = input("Enter new Genre: ")
            book.copies = int(input("Enter new Number of Copies: "))
            print("Book updated successfully!")
            return
    print("Book not found.")

# Function to delete a book

def delete_book(books):

    delete_id = input("Enter Book ID to delete: ")
    for book in books:
        if book.book_id == delete_id:
            books.remove(book)
            print("Book deleted successfully!")
            return
    print("Book not found.")

# Function to save books to a binary file

def save_books_to_binary_file(books):

    with open('books.dat', 'wb') as file:
        pickle.dump(books, file)

    print("Books saved to binary file.")

# Function to load books from a binary file

def load_books_from_binary_file():

    try:
        with open('books.dat', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
#Function to save books to a CSV file

def save_books_to_csv_file(books):

    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Book ID", "Title", "Author", "Genre", "Copies"])
        for book in books:
            writer.writerow([book.book_id, book.title, book.author, book.genre, book.copies])
    print("Books saved to CSV file.")

# Function to load books from a CSV file

def load_books_from_csv_file():

    try:
        with open('books.csv', 'r') as file:
            reader = csv. DictReader(file)
            books = []
            for row in reader:
                book = Book(row['Book ID'], row['Title'], row['Author'],
                row['Genre'], int(row['Copies']))
                books.append(book)
                return books
    except FileNotFoundError:
        return []

# Function to view statistics

def view_statistics (books):

    print("\nLibrary Statistics:")
    print(f"Total Books: {len(books)}")
    total_copies = sum(book.copies for book in books)
    print(f"Total Copies: {total_copies}")

# Function to clear all data

def clear_all_data(books):
    confirm = input("""Are you sure you want to clear all data? (yes/no): """).lower()
    if confirm == 'yes':
        books.clear()
        print("All data cleared.")

    else:
         print("Operation canceled.")


# Function to check out a book

def check_out_book(books, checked_out_books):
    book_id = input("Enter Book ID to check out: ")
    for book in books:

        if book.book_id == book_id and book.copies > 0:
           patron_name = input("Enter Patron Name: ")
           due_date = input("Enter Due Date (YYYY-MM-DD): ")
           checked_out_book =CheckedOutBook(book_id, patron_name, due_date)
           checked_out_books.append(checked_out_book)
           book.copies = 1
           print(f"""Book checked out successfully to {patron_name}.
           Due date: {due_date}""")
           return
        elif book.book_id == book_id and book.copies == 0:
            print("No copies available for check out.")
            return
    print("Book not found.")

# Function to return a book

def return_book(books, checked_out_books):
    book_id= input("Enter Book ID to return: ")
    for checked_out_book in checked_out_books:
        if checked_out_book.book_id == book_id:
            for book in books:

                if book.book_id == book_id:
                    book.copies += 1
                    print("Book returned successfully.")
                    checked_out_books.remove(checked_out_book)
                    return
            print("Book not found.")
            return
    print("Book is not checked out.")

# Function to view checked-out books

def view_checked_out_books(checked_out_books):
    print("\nChecked-Out Books:")

    for checked_out_book in checked_out_books:
        print(f"""Book ID: {checked_out_book.book_id},
        Patron Name: {checked_out_book.patron_name}, Due Date: {checked_out_book.due_date}""")

# Function to save checked-out books to a file
def save_checked_out_books_to_file(checked_out_books):
    with open('checked_out_books.dat', 'wb') as file:
        pickle.dump(checked_out_books, file)

    print("Checked-out books saved to binary file.")

# Function to load checked-out books from a file

def load_checked_out_books_from_file():


    try:
        with open('checked_out_books.dat', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

# Function to add a patron

def add_patron(patrons):

    patron_name = input("Enter Patron Name: ")
    patrons.add(patron_name)
    print(f"Patron {patron_name} added successfully!")

# Function to view patrons

def view_patrons(patrons):

    print("\nPatron List:")
    for patron in patrons:
        print(patron)

# Function to save patrons to a file

def save_patrons_to_file(patrons):

    with open('patrons.dat', 'wb') as file:
        pickle.dump(patrons, file)
    print("Patrons saved to binary file.")

# Function to load patrons from a file

def load_patrons_from_file():

    try:
    
        with open('patrons.dat', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:

        return set()

# Main function

def main():

    books = load_books_from_binary_file()
    checked_out_books = load_checked_out_books_from_file()
    patrons =load_patrons_from_file()
    while True:
        display_menu()
        choice = input("Enter your choice (1-21): ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            update_book(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            save_books_to_binary_file(books)
        elif choice == '7':
            books= load_books_from_binary_file()
            print("Books loaded from binary file.")
        elif choice == '8':
            save_books_to_csv_file(books)
        elif choice == '9':

            books=load_books_from_csv_file() 
            print("Books loaded from CSV file.")
        elif choice == '10':
            view_statistics(books)
        elif choice == '11':
            clear_all_data(books)
        elif choice == '12':
            check_out_book (books, checked_out_books)
    
        elif choice == '13':

            return_book(books, checked_out_books)

        elif choice == '14':

            view_checked_out_books(checked_out_books)

        elif choice == '15':

            save_checked_out_books_to_file(checked_out_books)
        elif choice == '16':
            checked_out_books = load_checked_out_books_from_file()
            print("Checked-out books loaded from binary file.")
        elif choice == '17':
            add_patron(patrons)
        elif choice == '18':

            view_patrons (patrons)

        elif choice == '19':

            save_patrons_to_file(patrons)

        

        elif choice == '20':
            patrons = load_patrons_from_file()
            print("Patrons loaded from binary file.")
        elif choice == '21':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("""Invalid choice.
            Please enter a number between 1 and 21.""")
if __name__ == "__main__":
    main()  
