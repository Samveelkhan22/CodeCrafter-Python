class LibraryManagementSystem:
    def __init__(self):
        # Dictionary to store books by category
        self.books = {
            "Fiction": [
                {"title": "1984", "author": "George Orwell", "available": True},
                {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True},
            ],
            "Science": [
                {"title": "A Brief History of Time", "author": "Stephen Hawking", "available": True},
                {"title": "The Selfish Gene", "author": "Richard Dawkins", "available": True},
            ],
        }
        # Set to track borrowed books
        self.borrowed_books = set()

    def display_books(self):
        print("Available Books by Category:")
        for category, books in self.books.items():
            print(f"\nCategory: {category}")
            for book in books:
                if book["available"]:
                    print(f" - {book['title']} by {book['author']}")

    def borrow_book(self, title):
        for category, books in self.books.items():
            for book in books:
                if book["title"] == title:
                    if book["available"]:
                        book["available"] = False
                        self.borrowed_books.add(title)
                        print(f"\nYou have borrowed: {title}")
                        return
                    else:
                        print(f"\nThe book '{title}' is already borrowed.")
                        return
        print(f"\nThe book '{title}' is not found in the library.")

    def return_book(self, title):
        if title in self.borrowed_books:
            for category, books in self.books.items():
                for book in books:
                    if book["title"] == title:
                        book["available"] = True
                        self.borrowed_books.remove(title)
                        print(f"\nYou have returned: {title}")
                        return
        print(f"\nThe book '{title}' was not borrowed.")

    def list_borrowed_books(self):
        print("\nBorrowed Books:")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(f" - {book}")
        else:
            print("No books are currently borrowed.")

# Example Usage
library = LibraryManagementSystem()
library.display_books()

library.borrow_book("1984")
library.borrow_book("The Great Gatsby")
library.borrow_book("1984")  # Trying to borrow again

library.list_borrowed_books()

library.return_book("1984")
library.return_book("The Catcher in the Rye")  # Invalid return
library.list_borrowed_books()

library.display_books()
