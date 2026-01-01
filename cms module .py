# Personal Contact Management System

contacts = []  #store contact

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    #duplicate phone number
    for contact in contacts:
        if contact["phone"] == phone:
            print("A contact with this phone number already exists!")
            return

    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\nAll Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact():
    search_term = input("Enter Name or Phone to Search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact["phone"]:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    phone = input("Enter Phone of the Contact to Update: ")
    for contact in contacts:
        if contact["phone"] == phone:
            new_name = input("Enter New Name (leave blank to keep the same): ")
            new_phone = input("Enter New Phone (leave blank to keep the same): ")
            new_email = input("Enter New Email (leave blank to keep the same): ")

            if new_phone and any(c["phone"] == new_phone for c in contacts if c != contact):
                print("Another contact with this phone number already exists!")
                return

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email

            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    phone = input("Enter Phone of the Contact to Delete: ")
    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")