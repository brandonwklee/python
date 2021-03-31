from contactBook import addDetails, displayDetails, deleteDetails

contact_book = []
company_book = []

def menu():
    number = [1, 2, 3, 4, 5, 6]
    option = ['add contact', 'add business contact', 'view contacts', 'view businesses', 'delete contact', 'quit']
    i = 0;
    print('----------------------------------\n')
    print("PHONEBOOK\n")
    print('select your option below: ')
    while (i + 1 < 7):
        print(number[i], ':', option[i])
        i+= 1
    print()
    choice = int(input('enter your option: '))
    if (choice == 1):
        addDetails.add_contact()

    if (choice == 2):
        addDetails.add_company()

    if (choice == 3):
        if not contact_book:
            print()
            print('contact book is empty!\n')
            menu()
        else:
            displayDetails.show_contacts()

    if (choice == 4):
        if not company_book:
            print()
            print('company book is empty!\n')
            menu()
        else:
            displayDetails.show_companies()

    if (choice == 5):
        if not contact_book and not company_book:
            print()
            print('contact book and company book are empty!\n')
            menu()
        else:
            deleteDetails.delete_details()

    if (choice == 6):
        quit()


if __name__ is '__main__':
    menu()