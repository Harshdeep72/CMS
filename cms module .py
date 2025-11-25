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
