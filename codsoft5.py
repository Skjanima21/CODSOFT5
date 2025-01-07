contacts = {}
def add_contact():
    """Add a new contact."""
    name = input("\nEnter name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()
    address = input("Enter address (optional): ").strip()
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")
def view_contacts():
    """Display all contacts."""
    if not contacts:
        print("\nNo contacts found!")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
def search_contact():
    """Search for a contact by name or phone number."""
    query = input("\nEnter name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["phone"]:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details.get('email', 'N/A')}")
            print(f"Address: {details.get('address', 'N/A')}")
            found = True
    if not found:
        print("No matching contact found!")
def update_contact():
    """Update an existing contact."""
    name = input("\nEnter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    print("\nLeave a field blank to keep the current value.")
    phone = input("Enter new phone number: ").strip() or contacts[name]["phone"]
    email = input("Enter new email: ").strip() or contacts[name]["email"]
    address = input("Enter new address: ").strip() or contacts[name]["address"]
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact updated successfully!")
def delete_contact():
    """Delete a contact."""
    name = input("\nEnter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")
def main():
    """Main function for the Contact Book application."""
    print("Welcome to the Contact Book!")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")
if __name__ == "__main__":
    main()
