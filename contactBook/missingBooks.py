from contactBook import phoneBook, deleteDetails

def no_company_book():
    number = [1, 2]
    options = ['contact book', 'back to main menu']
    i = 0
    print()
    while (i < len(number)):
        print(number[i], ':', options[i])
        i += 1
    print()
    choice = int(input('enter your option: '))
    if (choice == 1):
        deleteDetails.delete_contact_info()
    if (choice == 2):
        phoneBook.menu()

def no_contact_book():
    number = [1, 2]
    options = ['company book', 'back to main menu']
    i = 0
    print()
    while (i < len(number)):
        print(number[i], ':', options[i])
        i += 1
    choice = int(input('enter your option: '))
    print()
    if (choice == 1):
        deleteDetails.delete_company_info()
    if (choice == 2):
        phoneBook.menu()
