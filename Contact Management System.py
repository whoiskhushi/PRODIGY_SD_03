class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Contact found. Enter new details.")
                contact.name = input("Enter new name: ")
                contact.phone = input("Enter new phone: ")
                contact.email = input("Enter new email: ")
                print("Contact updated.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted.")
                return
        print("Contact not found.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to edit: ")
            manager.edit_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
