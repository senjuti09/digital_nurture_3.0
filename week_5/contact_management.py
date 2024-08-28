import pickle

def read_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            contacts = file.readlines()
        return [contact.strip() for contact in contacts]
    except FileNotFoundError:
        return []

def write_contacts(file_name, contacts):
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

def add_contact(file_name, contact):
    contacts = read_contacts(file_name)
    contacts.append(contact)
    write_contacts(file_name, contacts)

def remove_contact(file_name, contact):
    contacts = read_contacts(file_name)
    if contact in contacts:
        contacts.remove(contact)
        write_contacts(file_name, contacts)
        print(f"{contact} has been removed.")
    else:
        print(f"{contact} not found.")

def display_contacts(file_name):
    contacts = read_contacts(file_name)
    if contacts:
        print("Contacts List:")
        for contact in contacts:
            print(contact)
    else:
        print("No contacts found.")

def save_contacts_binary(file_name, contacts):
    with open(file_name, 'wb') as file:
        pickle.dump(contacts, file)

def load_contacts_binary(file_name):
    try:
        with open(file_name, 'rb') as file:
            contacts = pickle.load(file)
        return contacts
    except (FileNotFoundError, EOFError):
        return []

def user_interaction(file_name, binary=False):
    while True:
        choice = input("\n1: Add Contact\n2: Remove Contact\n3: Display Contacts\n4: Quit\nChoose an option: ")
        
        if choice == '1':
            contact = input("Enter contact name: ")
            if binary:
                contacts = load_contacts_binary(file_name)
                contacts.append(contact)
                save_contacts_binary(file_name, contacts)
            else:
                add_contact(file_name, contact)
        
        elif choice == '2':
            contact = input("Enter contact name to remove: ")
            if binary:
                contacts = load_contacts_binary(file_name)
                if contact in contacts:
                    contacts.remove(contact)
                    save_contacts_binary(file_name, contacts)
                    print(f"{contact} has been removed.")
                else:
                    print(f"{contact} not found.")
            else:
                remove_contact(file_name, contact)
        
        elif choice == '3':
            if binary:
                contacts = load_contacts_binary(file_name)
                if contacts:
                    print("Contacts List:")
                    for contact in contacts:
                        print(contact)
                else:
                    print("No contacts found.")
            else:
                display_contacts(file_name)
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    file_name = "contacts.txt"
    binary_file_name = "contacts.dat"
    
    print("Text File Operations")
    user_interaction(file_name)
    
    print("\nBinary File Operations")
    user_interaction(binary_file_name, binary=True)
