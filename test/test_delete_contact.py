from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Aneta"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# test przed zmianami zaciągania danych z bazy danych
#def test_delete_some_contact(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="Aneta"))
    #old_contacts = app.contact.get_contact_list()
    #index = randrange(len(old_contacts))
    #app.contact.delete_contact_by_index(index)
    #assert len(old_contacts) - 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()



#def test_delete_first_contact(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="Aneta"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.delete_first_contact()
    #assert len(old_contacts) - 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()



