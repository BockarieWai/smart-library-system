# demo.py

from operations import *

# --- Add books ---
print(add_new_book("BK001", "Learning Python", "Mark Lutz", "Education", 3))
print(add_new_book("BK002", "The Martian", "Andy Weir", "Science", 4))
print(add_new_book("BK003", "Animal Farm", "George Orwell", "Fiction", 2))
print(add_new_book("BK004", "A Brief History of Time", "Stephen Hawking", "Science", 3))

# --- Add members ---
print(add_user("U001", "Mr. Wai", "wai@example.com"))
print(add_user("U002", "John T. Kallon", "kallonjr@example.com"))
print(add_user("U003", "Sally Jones", "sallyj@example.com"))

# --- Search by author ---
print("\n Search for author 'George':")
print(lookup_book("George", field="author"))

# --- Borrow books ---
print(issue_book("U001", "BK001"))
print(issue_book("U001", "BK003"))
print(issue_book("U002", "BK002"))

# --- Return a book ---
print(receive_book("U001", "BK001"))

# --- Try to delete book/member with pending borrows ---
print(remove_book_record("BK003"))   # Should fail
print(remove_user("U001"))           # Should fail (still has borrowed book)

# --- Update user ---
print(edit_user("U002", Email="kallonjr2025@example.com"))

# --- Final Data ---
print("\n Books Database:")
print(books_db)

print("\n Users Database:")
print(users_db)
