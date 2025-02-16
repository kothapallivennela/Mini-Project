class Book:
    def __init__(self, book_id, title, author, count):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.count = count

    def __str__(self):
        return f"{self.book_id}: {self.title} by {self.author} (Count: {self.count})"

class Bookstore:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author, count):
        if book_id in self.books:
            self.books[book_id].count += count
        else:
            self.books[book_id] = Book(book_id, title, author, count)
        print("Book added/updated successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            for book in self.books.values():
                print(book)

    def purchase_book(self, book_id):
        if book_id not in self.books:
            print("Book not found.")
        elif self.books[book_id].count == 0:
            print("Book is out of stock.")
        else:
            self.books[book_id].count -= 1
            print(f"Successfully purchased '{self.books[book_id].title}'.")
            if self.books[book_id].count == 0:
                print(f"'{self.books[book_id].title}' is now out of stock.")

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book deleted successfully!")
        else:
            print("Book not found.")

    def exit_system(self):
        print("THANK YOU!")
        exit()

def main():
    bookstore = Bookstore()

    while True:
        print("\nBookstore Management System")
        print("1. View Books")
        print("2. Add/Update Book")
        print("3. Purchase Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            bookstore.view_books()
        elif choice == '2':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            count = int(input("Enter Count: "))
            bookstore.add_book(book_id, title, author, count)
        elif choice == '3':
            book_id = input("Enter Book ID to purchase: ")
            bookstore.purchase_book(book_id)
        elif choice == '4':
            book_id = input("Enter Book ID to delete: ")
            bookstore.delete_book(book_id)
        elif choice == '5':
            bookstore.exit_system()
        else:
            print("Invalid choice try again.")

if __name__ == "__main__":
    main()