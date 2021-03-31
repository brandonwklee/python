from contactBook import phoneBook, contacts

def add_contact():
    print('----------------------------------\n')
    print('adding contact\n')
    name = str(input('enter name: '))
    if (name =='quit'):
        phoneBook.menu()
    number = int(input('enter phone number: '))
    email = str(input('enter email: '))
    contact_info = contacts.contactDetails(name, number, email)
    phoneBook.contact_book.append(contact_info)
    print()
    phoneBook.menu()

def add_company():
    print('----------------------------------\n')
    name = str(input('enter name: '))
    number = int(input('enter phone number: '))
    email = str(input('enter email: '))
    business = str(input('enter business name: '))
    company_details = contacts.company(name, number, email, business)
    phoneBook.company_book.append(company_details)
    print()
    phoneBook.menu()