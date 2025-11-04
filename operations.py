# operations.py

books_db = {}      # Key: ISBN → value: dict of details
users_db = []      # List of members
CATEGORIES = ["Fiction", "Non-Fiction", "Science", "Education"]

# -------------------- Book Functions -------------------- #

def add_new_book(isbn, title, author, category, copies):
    """Insert a book record into the database."""
    if isbn in books_db:
        return f"Error: Book {isbn} already exists."
    if category not in CATEGORIES:
        return "Invalid book category."

    books_db[isbn] = {
        "Title": title,
        "Author": author,
        "Category": category,
        "TotalCopies": copies,
        "AvailableCopies": copies
    }
    return f"Book '{title}' added successfully."


def lookup_book(term, field="title"):
    """Find books by title or author."""
    term = term.lower()
    results = []
    for code, info in books_db.items():
        if field == "title" and term in info["Title"].lower():
            results.append((code, info))
        elif field == "author" and term in info["Author"].lower():
            results.append((code, info))
    return results


def remove_book_record(isbn):
    """Delete a book if all copies are available."""
    if isbn not in books_db:
        return "Book not found."
    if books_db[isbn]["AvailableCopies"] != books_db[isbn]["TotalCopies"]:
        return "Cannot remove book while copies are on loan."
    del books_db[isbn]
    return f"Book {isbn} deleted from records."


# -------------------- Member Functions -------------------- #

def add_user(member_id, full_name, email):
    """Register a new user in the system."""
    for user in users_db:
        if user["MemberID"] == member_id:
            return "Duplicate member ID found."
    users_db.append({
        "MemberID": member_id,
        "Name": full_name,
        "Email": email,
        "Borrowed": []
    })
    return f"User {full_name} registered successfully."


def edit_user(member_id, **kwargs):
    """Update user details such as email or name."""
    for user in users_db:
        if user["MemberID"] == member_id:
            user.update(kwargs)
            return f"Member {member_id} updated successfully."
    return "Member not found."


def remove_user(member_id):
    """Remove a user only if they have no active borrowed books."""
    for user in users_db:
        if user["MemberID"] == member_id:
            if user["Borrowed"]:
                return "Cannot remove user with borrowed books."
            users_db.remove(user)
            return f"Member {member_id} removed from records."
    return "Member not found."


# -------------------- Borrowing Functions -------------------- #

def issue_book(member_id, isbn):
    """Lend a book to a registered member."""
    if isbn not in books_db:
        return "Book not found in records."
    if books_db[isbn]["AvailableCopies"] == 0:
        return "No copies left to borrow."

    for user in users_db:
        if user["MemberID"] == member_id:
            user["Borrowed"].append(isbn)
            books_db[isbn]["AvailableCopies"] -= 1
            return f"{user['Name']} borrowed '{books_db[isbn]['Title']}'."
    return "Member not found."


def receive_book(member_id, isbn):
    """Return a borrowed book."""
    for user in users_db:
        if user["MemberID"] == member_id:
            if isbn not in user["Borrowed"]:
                return "Book not borrowed by this user."
            user["Borrowed"].remove(isbn)
            books_db[isbn]["AvailableCopies"] += 1
            return f"{user['Name']} returned '{books_db[isbn]['Title']}'."
    return "Member not found."
