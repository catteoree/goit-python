class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        dict_user = {}
        dict_user = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
        self.contacts.append(dict_user)
        Contacts.current_id += 1


contact_book = Contacts()
second_contact_book = Contacts()

contact_book.add_contacts('Vasyl', '1234', 'vasyl@root.com', True)
contact_book.add_contacts('Andrew', '5555', 'andrew@root.com', True)
print(contact_book.current_id)
contact_book.add_contacts('Yura', '3251', 'yura@root.com', True)
print(contact_book.list_contacts())
print(second_contact_book.current_id)
