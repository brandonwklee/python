from contactBook import phoneBook, missingBooks

def delete_details():
    print('----------------------------------\n')
    number = [1, 2, 3]
    options = ['contact book', 'company book', 'back to main menu']
    i = 0
    if not phoneBook.contact_book:
        missingBooks.no_contact_book()

    elif not phoneBook.company_book:
        print('no entries found in company book')
        missingBooks.no_company_book()

    while (i < len(number)):
        print(number[i], ':', options[i])
        i += 1
    print()
    choice = int(input('enter your option: '))
    if (choice == 1):
        delete_contact_info()
    if (choice == 2):
        delete_company_info()
    if (choice == 3):
        phoneBook.menu()


def delete_contact_info():
    try:
        while phoneBook.contact_book != []:
            print('----------------------------------\n')
            print('lists of contacts: \n')
            for i in range(0, len(phoneBook.contact_book)):
                print('Contact', i, '-', phoneBook.contact_book[i])
            print()
            choice = input('enter the contact number to delete the details or enter ''q'' to exit: ')
            if (choice.isdigit()):
                choice = int(choice)
                if (phoneBook.contact_book[choice]):
                    del phoneBook.contact_book[choice]
            if (phoneBook.contact_book == [] and phoneBook.company_book != []):
                missingBooks.no_contact_book()
            elif (phoneBook.contact_book == [] and phoneBook.company_book == []):
                phoneBook.menu()
            if (choice == 'q' or choice == 'Q'):
                if (phoneBook.contact_book != [] and phoneBook.company_book != []):
                    delete_details()
                elif (phoneBook.contact_book == [] and phoneBook.company_book != []):
                    missingBooks.no_contact_book()
                elif (phoneBook.contact_book != [] and phoneBook.company_book == []):
                    missingBooks.no_company_book()
    except IndexError as error:
        print()
        print(error, 'in contact book')
        print()
        delete_contact_info()

def delete_company_info():
    try:
        while phoneBook.company_book != []:
            print('----------------------------------\n')
            print('lists of companies: \n')
            for i in range(0, len(phoneBook.company_book)):
                print('Contact', i, '-', phoneBook.company_book[i])
            print()
            choice = input('enter the contact number to delete the details of the company or enter ''q'' to exit: ')
            if (choice.isdigit()):
                choice = int(choice)
                if (phoneBook.company_book[choice]):
                    del phoneBook.company_book[choice]
            if (phoneBook.contact_book == [] and phoneBook.company_book != []):
                missingBooks.no_contact_book()
            elif (phoneBook.contact_book == [] and phoneBook.company_book == []):
                phoneBook.menu()
            if (choice == 'q' or choice == 'Q'):
                if (phoneBook.contact_book != [] and phoneBook.company_book != []):
                    delete_details()
                elif (phoneBook.contact_book == [] and phoneBook.company_book != []):
                    missingBooks.no_contact_book()
                elif (phoneBook.contact_book != [] and phoneBook.company_book == []):
                    missingBooks.no_company_book()
    except IndexError as error:
        print()
        print(error, 'in company book')
        print()
        delete_company_info()