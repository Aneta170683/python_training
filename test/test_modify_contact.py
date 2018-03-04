from model.contact import Contact
import random



def test_modify_contact_firstname(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Aneta", lastname="Kwiatek"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id, new_contact_data=Contact(firstname="Anetka", lastname="Prokop"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()


#def test_modify_contact_lastname(app):
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(lastname="Kowalska"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
