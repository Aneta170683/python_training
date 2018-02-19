from model.contact import Contact
from random import randrange



def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Aneta", lastname="Kwiatek"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.modify_contact_by_index(index, Contact(firstname="Anetka", lastname="Prokop"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()


#def test_modify_contact_lastname(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(lastname="Kowalska"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
