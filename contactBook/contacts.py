class contactDetails:

    def __init__(self, name, number, email):
        self.__name = name
        self.__number = number
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return 'Name: ' + self.__name + ' ' + 'number: ' + str(self.__number) + ' ' + 'email: ' + self.__email


class company(contactDetails):

    def __init__(self, name, number, email, company):
        contactDetails.__init__(self, name, number, email)
        self.__company = company

    def set_company(self, company):
        self.__company = company

    def __str__(self):
        return super().__str__() + ' company: ' + self.__company