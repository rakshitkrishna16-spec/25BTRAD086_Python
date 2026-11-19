contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added: {name}")

def search_contact(name):
    if name in contacts:
        print(f"Found: {name} -> {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Deleted: {name}")

add_contact("Alice", "9876543210")
add_contact("Bob", "9123456789")
search_contact("Alice")
delete_contact("Bob")