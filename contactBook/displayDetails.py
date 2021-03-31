from contactBook import phoneBook

def show_contacts():
    print('----------------------------------\n')
    for i in range(0, len(phoneBook.contact_book)):
        print('contact', i)
        print(phoneBook.contact_book[i])
        print()
    phoneBook.menu()

def show_companies():
    print('----------------------------------\n')
    for i in range(0, len(phoneBook.company_book)):
        print('company', i)
        print(phoneBook.company_book[i])
    phoneBook.menu()
