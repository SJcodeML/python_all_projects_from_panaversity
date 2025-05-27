import json
import os

# Optional: Load existing library data from a file if it exists
file_name = 'library.json'
if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        books = json.load(file)
else:
    books = []

def save_library():
    """Save the current library to a JSON file."""
    with open(file_name, 'w') as file:
        json.dump(books, file, indent=4)

while True:
    print("\n--- Personal Library Manager ---")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Save and Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # Add a book
        print("\nAdding a New Book")
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        while True:
            try:
                year = int(input("Publication Year: "))
                break
            except ValueError:
                print("Please enter a valid year.")
        genre = input("Genre: ").strip()
        read_input = input("Have you read it? (yes/no): ").strip().lower()
        read_status = 'yes' if read_input in ['yes', 'y'] else 'no'
        new_book = {
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'read': read_status
        }
        books.append(new_book)
        print(f'"{title}" added to your library.')

    elif choice == '2':
        # Remove a book
        remove_title = input("\nEnter the title of the book to remove: ").strip()
        for b in books:
            if b['title'].lower() == remove_title.lower():
                books.remove(b)
                print(f'"{b["title"]}" removed successfully.')
                break
        else:
            print("Book not found.")

    elif choice == '3':
        # Search for a book
        print("\nSearch by: 1. Title  2. Author")
        sub_choice = input("Enter choice (1 or 2): ").strip()
        if sub_choice == '1':
            search_title = input("Enter the title: ").strip().lower()
            results = [b for b in books if b['title'].lower() == search_title]
        elif sub_choice == '2':
            search_author = input("Enter the author: ").strip().lower()
            results = [b for b in books if b['author'].lower() == search_author]
        else:
            print("Invalid choice.")
            continue

        if results:
            print("\nFound the following books:")
            for b in results:
                print(f"Title: {b['title']} | Author: {b['author']} | Year: {b['year']} | Genre: {b['genre']} | Read: {b['read'].capitalize()}")
        else:
            print("No matches found.")

    elif choice == '4':
        # Display all books
        if not books:
            print("\nYour library is empty.")
        else:
            print("\nYour Library Books:")
            for i, b in enumerate(books, 1):
                print(f"{i}. Title: {b['title']} | Author: {b['author']} | Year: {b['year']} | Genre: {b['genre']} | Read: {b['read'].capitalize()}")

    elif choice == '5':
        # Statistics
        total = len(books)
        read_count = sum(1 for b in books if b['read'] == 'yes')
        unread_count = total - read_count
        print(f"\nLibrary Statistics:\nTotal books: {total}\nRead: {read_count}\nUnread: {unread_count}")

    elif choice == '6':
        # Save and exit
        save_library()
        print("Library saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")