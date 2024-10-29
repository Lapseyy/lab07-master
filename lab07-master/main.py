import contacts

def main():
    # Initialize Contacts object with a default filename
    contact_list = contacts.Contacts("default_contacts.json")
    # contact_list = {}
    while True:
       # contact_list = {}
        # Display the menu
        print("\nTuffy Titan Contact List Menu")
        print("1. Add contact")
        print("2. Modify contact")
        print("3. Delete contact")
        print("4. Print contact list")
        print("5. Set contact filename")
        print("6. Exit")

        # Prompt user for menu choice
        choice = input("Enter menu choice: ")

        if choice == '1':  # Add contact
            id = input("Enter contact ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            result = contact_list.add_contact(id, first_name, last_name)
            if result == "error":
                print("Error: Contact ID already exists.")
            else:
                print(f"Contact added: {result}")

        elif choice == '2':  # Modify contact
            id = input("Enter contact ID to modify: ")
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            result = contact_list.modify_contact(id=id, first_name=first_name, last_name=last_name)
            if result == "error":
                print("Error: Contact ID does not exist.")
            else:
                print(f"Contact modified: {result}")

        elif choice == '3':  # Delete contact
            id = input("Enter contact ID to delete: ")
            result = contact_list.delete_contact(id=id)
            if result == "error":
                print("Error: Contact ID does not exist.")
            else:
                print(f"Contact deleted: {result}")

        elif choice == '4':  # Print contact list
            if not contact_list.data:
                print("No contacts available.")
            else:
                # Print header
                print("     ==================== CONTACT LIST ====================")
                print("     Last Name             First Name            Phone")
                print("     ====================  ====================  ============")

                # Print each contact, formatted
                for id, contact in contact_list.data.items():
                    if len(contact) == 2:
                        first_name, last_name = contact
                        print(f"     {last_name:<20}  {first_name:<20}  {id:<10}")
                    else:
                        print(f"ID: {id}, Invalid contact format")


        elif choice == '5':  # Set contact filename
            filename = input("Enter new filename (e.g., contacts.json): ")
            contact_list = contacts.Contacts(filename)
            print(f"Contact file set to: {filename}")

        elif choice == '6':  # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
