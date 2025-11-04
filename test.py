# test_operations.py
# Automated tests for Smart Library Management System - Version 3
from operations import *

def run_tests():
    print(" Running Smart Library Tests...\n")

    assert "successfully" in add_new_book("TST001", "Code Complete", "Steve McConnell", "Education", 2)
    assert "successfully" in add_user("MEM001", "Test User", "testuser@example.com")

    assert "borrowed" in issue_book("MEM001", "TST001")
    assert "returned" in receive_book("MEM001", "TST001")

    assert len(lookup_book("Code", field="title")) > 0
    assert "deleted" in remove_book_record("TST001")
    assert "removed" in remove_user("MEM001")

    print("✅ All tests passed successfully.")

if __name__ == "__main__":
    run_tests()
