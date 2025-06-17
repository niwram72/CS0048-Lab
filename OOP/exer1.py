class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            return f'You have borrowed "{self.title}"'
        return f'Sorry, {self.title} is not available.'
    
    def return_book(self):
        self.available = True
        return f'Returned {self.title}'
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f'{self.title} by {self.author} - {status}'

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return f'Book "{title}" added successfully.'
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow()
        return f'Book "{title}" not found.'
    
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f'Book "{title}" not found.'
    
    def view_books(self):
        if not self.books:
            return '\nNo books in the library.'
        return "\n".join(str(book) for book in self.books)
        
def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Books")
        print("5. Exit")
        
        choice = input("Enter choice 1-5: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            print(library.add_book(title, author))
        elif choice == '2':
            title = input("Enter book title to borrow: ")
            print(library.borrow_book(title))
        elif choice == '3':
            title = input("Enter book title to return: ")
            print(library.return_book(title))
        elif choice == '4':
            print(library.view_books())
        elif choice == '5':
            print("Thank you for using the program.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()