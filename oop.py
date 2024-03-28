class Book:
    def __init__(self, title, author):
        # Initialize a Book object with title and author
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        # Initialize Library object with an empty list of books
        self.books = []

    def add_book(self, title, author):
        # Add a new book to the library
        book = Book(title, author)
        self.books.append(book)

    def list_all_books(self):
        # List all the books in the library
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book.title} by {book.author}")

    def search_by_title(self, title):
       # Search for books by title
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not found_books:
            print("No books found with that title.")
        else:
            print(f"Books with title '{title}':")
            for book in found_books:
                print(f"{book.title} by {book.author}")

    def search_by_author(self, author):
        """Search for books by author."""
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if not found_books:
            print("No books found by that author.")
        else:
            print(f"Books by author '{author}':")
            for book in found_books:
                print(f"{book.title} by {book.author}")

# Example usage:
library = Library()

while True:
    print("\nMenu:")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Search books by title")
    print("4. Search books by author")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        library.add_book(title, author)
        print("Book added successfully!")

    elif choice == '2':
        library.list_all_books()

    elif choice == '3':
        title = input("Enter the title to search: ")
        library.search_by_title(title)

    elif choice == '4':
        author = input("Enter the author to search: ")
        library.search_by_author(author)

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
