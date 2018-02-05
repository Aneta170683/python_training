from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Aneta", lastname="Kwiatek"))
    app.contact.modify_first_contact(Contact(firstname="Antonina"))


def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Kowalska"))